#coding=utf-8
from flask_cors import CORS
from flask import Flask,jsonify,request
import sys
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

@app.route("/GetPageSet",methods=['POST'])
# 使用pymysql指令來連接數據庫
def GetPageSet():
    m_sql=Sql.sql()
    Note = request.json.get("Note")
    result = m_sql.GetDataRow("SELECT * FROM PageSet WHERE Page= %s" ,(Note))
    return "" if result == None else result
    
    app.run()
