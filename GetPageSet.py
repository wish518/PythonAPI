#coding=utf-8
from flask_cors import CORS
from flask import Flask,jsonify,request
import sys
import json
sys.path.append('./Common')
import SettingData
import Sql
import Email
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

@app.route("/SetMessage",methods=['POST'])
# 使用pymysql指令來連接數據庫
def SetMessage():
    Func = request.json.get("Func")
    Message = request.json.get("Message")
    result =SettingData.result
    try:
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
           ClientIP = request.environ['REMOTE_ADDR']
        else:
           ClientIP = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    
        m_sql=Sql.sql()
        result = m_sql.GetDataRow("CALL Ins_Message(%s,'Guest','N',%s,%s)" ,(Func,Message,ClientIP))

        m_Email=Email.Email()
        return m_Email.SendGmail("wishwise518@gmail.com" ,"TrueEuqal1留言通知","<h3>" +Func + " 有新留言</h3> Guest 說:<div style='white-space: break-spaces;'>" + Message+"</div>")
        
    except Exception as e:
        return json.dumps({"Code":"999"},  default=str)
        
    return json.dumps(result,  default=str)

@app.route("/GetMessage",methods=['POST'])
# 使用pymysql指令來連接數據庫
def GetMessage():
    Func = request.json.get("Func")
    m_sql=Sql.sql()
    result =  m_sql.GetDataTable("SELECT * FROM Message WHERE Func = %s ORDER BY Sort" ,(Func))
    return json.dumps(result,  default=str)

  
