import pymysql
from flask import Flask
import sys
sys.path.append('Common')
import Sql
#from json import jsonify

app = Flask(__name__)
@app.route("/")
# 使用pymysql指令來連接數據庫
def hello():
    m_sql=Sql.sql()
    return m_sql.GetDataRow("select * from pageset")
    #return "123"
