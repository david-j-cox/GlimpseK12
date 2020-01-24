from flask import render_template
from additional import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from time import sleep

user = 'dcox' #add your username here (same as previous postgreSQL)                      
host = 'localhost'
dbname = 'glimpse'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

@app.route('/')
@app.route('/index')
def index():
   user = { 'nickname': 'David' } # fake user
   return render_template("index.html", title = 'Home', user = user)

@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
   user = { 'nickname': 'David' } # fake user
   sleep(2)
   return render_template("teachers.html", title = 'Teachers')

@app.route('/db')
def match_Ozuna():
    sql_query = """                                                                       
                SELECT * FROM "glimpseTable" WHERE "GR"='6';          
                """
    query_results = pd.read_sql_query(sql_query,con)
    math_scores = []
    for i in range(0,100):
        m_scores = query_results.iloc[i]['ScantronMathPostTest']
        math_scores.append(m_scores)
    read_scores = []
    sleep(2)
    for i in range(0,100):
    	r_scores = query_results.iloc[i]['ScantronReadingPostTest']
    	read_scores.append(r_scores)
    return render_template("match.html", math_scores=math_scores, read_scores=read_scores)

@app.route('/db')
def match_Jeter():
    sql_query = """                                                                       
                SELECT * FROM "glimpseTable" WHERE "GR"='2';          
                """
    query_results = pd.read_sql_query(sql_query,con)
    math_scores = []
    for i in range(0,100):
        m_scores = query_results.iloc[i]['ScantronMathPostTest']
        math_scores.append(m_scores)
    read_scores = []
    for i in range(0,100):
    	r_scores = query_results.iloc[i]['ScantronReadingPostTest']
    	read_scores.append(r_scores)
    return render_template("match.html", math_scores=math_scores, read_scores=read_scores)

@app.route('/db')
def match_Walker():
    sql_query = """                                                                       
                SELECT * FROM "glimpseTable" WHERE "GR"='8';          
                """
    query_results = pd.read_sql_query(sql_query,con)
    math_scores = []
    for i in range(0,100):
        m_scores = query_results.iloc[i]['ScantronMathPostTest']
        math_scores.append(m_scores)
    read_scores = []
    for i in range(0,100):
    	r_scores = query_results.iloc[i]['ScantronReadingPostTest']
    	read_scores.append(r_scores)
    return render_template("match.html", math_scores=math_scores, read_scores=read_scores)