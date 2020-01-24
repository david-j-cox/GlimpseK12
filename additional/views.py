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
def match():
    sql_query = """                                                                       
                SELECT * FROM "glimpseTable" WHERE "GR"='6';          
                """
    query_results = pd.read_sql_query(sql_query,con)
    teachers = []
    for i in range(0,1000):
        teachers += query_results.iloc[i]['ScantronMathPostTest']
        teachers += "<br>"
    return teachers