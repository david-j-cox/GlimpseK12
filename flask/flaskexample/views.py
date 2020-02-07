from flask import render_template
from flaskexample import app
import pandas as pd
import psycopg2
from flask import request
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

username = 'dcox'                    
dbname = 'demodb'
password = 'postgres'
db = create_engine('postgres://%s@localhost/%s'%(username,dbname))
con=None
con = psycopg2.connect(database=dbname, user=username, host='localhost', password=password)


# Define functions
def get_stud_ID(GlimpseId):
	stud_id = {"1179":1179, "1221":1221, "1374":1374, "1660":1660, "1662":1662, "1694":1694, "1909":1909, 
	"46":46, "760":760, "811":811, "1208":1208, "1322":1322, "1420":1420, "4383":4383}
	return stud_id[GlimpseId]

def grade_choice(grade):
	grade_vals = {"3":3, "4":4, "5":5}
	return grade_vals[grade]

def math_prof(grade):
	math_proficiencies = {"3":2488, "4":2589, "5":2667}
	return math_proficiencies[grade]

def read_prof(grade):
	reading_proficiencies = {"3":2518, "4":2678, "5":2798}
	return reading_proficiencies[grade]

# App instructions
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
	return render_template("index.html")
 
@app.route('/predictions')
def predictions():
	if request.method == 'GET':
		GlimpseId = request.args.get('GlimpseId', '')
		stud_id = get_stud_ID(GlimpseId)
	if request.method == 'GET':
		grade = request.args.get('grade', '')
		grade_val = grade_choice(grade)
	if request.method == 'GET':
		proficiencies = request.args.get('grade', '')
		math_prof_val = math_prof(grade)
	if request.method == 'GET':
		proficiencies = request.args.get('grade', '')
		reading_prof_val = read_prof(grade)
	sql_query =  """SELECT  "TxRank", "TNUM", math_pred_cont, read_pred_cont, "IXLMathUser", "IXLReadingUser" FROM demo_top WHERE "GR" = '%s' AND "GlimpsestudentId" = '%s' """ %(grade_val, GlimpseId)
	query_results=pd.read_sql_query(sql_query, con)
	table_vals =[]
	for i in range(0,query_results.shape[0]):
		table_vals.append(dict(TxRank=query_results.iloc[i]['TxRank'], TNUM=query_results.iloc[i]['TNUM'], \
        	mathPred=query_results.iloc[i]['math_pred_cont'], readPred=query_results.iloc[i]['read_pred_cont'], mathTool=query_results.iloc[i]['IXLMathUser'], \
        	readTool=query_results.iloc[i]['IXLReadingUser']))
	return render_template('predictions.html', GlimpseId=stud_id, grade_level=grade_val, math_prof=math_prof_val, read_prof=reading_prof_val, table_vals=table_vals)



