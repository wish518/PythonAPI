#coding=utf-8
from flask_cors import CORS
from flask import Flask,jsonify
import sys
sys.path.append('./Common')
#sys.path.append('/var/www/html/PythonAPI/Common')
import Sql
#from json import jsonify

app = Flask(__name__)
CORS(app, resources={r"/.*": {"origins": ["http://127.0.0.1","https://127.0.0.1","http://127.0.0.1:3000"]}})
@app.route("/")
# 使用pymysql指令來連接數據庫
def hello():
    m_sql=Sql.sql()
    return m_sql.GetDataRow("select * from PageSet")
    #return "123"

    #app.run()
