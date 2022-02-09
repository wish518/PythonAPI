#coding=utf-8
from flask_cors import CORS
from flask import Flask,jsonify,request
import sys
import json
sys.path.append('./Common')
#sys.path.append('/var/www/html/PythonAPI/Common')
import Sql
#from json import jsonify
app = Flask(__name__)
CORS(app, resources={r"/.*": {"origins": ["http://trueequal.one","https://trueequal.one","http://127.0.0.1:3000","http://localhost:3000"]}})
@app.route("/")
# 使用pymysql指令來連接數據庫
def test():
    m_sql=Sql.sql()
    return 'Hollo peter'

@app.route("/Debug")
# 使用pymysql指令來連接數據庫
def Debug():
    m_sql=Sql.sql()
    return m_sql.GetDataRow("SELECT * FROM PageSet WHERE Page= 'test' " ,'')

@app.route("/GetPageSet",methods=['POST'])
# 使用pymysql指令來連接數據庫
def GetPageSet():
    m_sql=Sql.sql()
    Note = request.json.get("Note")
    result = m_sql.GetDataRow("SELECT * FROM PageSet WHERE Page= %s" ,(Note))
    return json.dumps([]) if result == None else json.dumps(result,  default=str)

@app.route("/GetMenuIndex",methods=['POST'])
# 使用pymysql指令來連接數據庫
def GetMenuIndex():
    m_sql=Sql.sql()
    result =  m_sql.GetDataTable("SELECT * FROM MenuIndex ORDER BY Sort" ,'')
    return json.dumps(result,  default=str)
  
