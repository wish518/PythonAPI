import pymysql
import threading
import SettingData
from dbutils.pooled_db import PooledDB
# connection = pymysql.connect(
#     host=SettingData.host,
#     user=SettingData.user,
#     password=SettingData.password,
#     db=SettingData.db,
#     charset=SettingData.charset,
#     cursorclass=pymysql.cursors.DictCursor,
# )
pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host=SettingData.host,  user=SettingData.user, password= SettingData.password, db=SettingData.db,  charset=SettingData.charset,)
lock = threading.Lock()
class sql: 
    # 使用pymysql指令來連接數據庫
    def GetDataRow(self, sqlStr,parms):
        try:
            lock.acquire()
            conn=pool.connection()
            # 從數據庫鏈接中得到cursor的數據結構
            with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                # 在之前建立的user表格基礎上，插入新數據，這裡使用了一個預編譯的小技巧，避免每次都要重複寫sql的語句
                # insert
                # sql="INSERT INTO `USERS`(`email`,`password`) VALUES (%s,%s)"
                # cursor.execute(sql,("webmaster@python.org’,’very_secret"))
                # 執行到這一行指令時才是真正改變了數據庫，之前只是緩存在內存中
                if(parms==''):
                   cursor.execute(sqlStr)
                else:
                   cursor.execute(sqlStr,parms)

                # 只取出一條結果
                result = cursor.fetchone()
                # 關閉 SQL 連線
                # 執行到這一行指令時才是真正改變了數據庫，之前只是緩存在內存中
                conn.commit()
                conn.close()
                lock.release()
                return result
        except Exception as e:
            return e.args[0]
            
    # 使用pymysql指令來連接數據庫
    def GetDataTable(self, sqlStr,parms):
        try:
            lock.acquire()
            conn=pool.connection()
            # 從數據庫鏈接中得到cursor的數據結構
            with  conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                # 在之前建立的user表格基礎上，插入新數據，這裡使用了一個預編譯的小技巧，避免每次都要重複寫sql的語句
                # insert
                # sql="INSERT INTO `USERS`(`email`,`password`) VALUES (%s,%s)"
                # cursor.execute(sql,("webmaster@python.org’,’very_secret"))
                # 執行到這一行指令時才是真正改變了數據庫，之前只是緩存在內存中
                if(parms==''):
                   cursor.execute(sqlStr)
                else:
                   cursor.execute(sqlStr,parms)

                # 只取出一條結果
                result = cursor.fetchall()
                # 關閉 SQL 連線
                conn.close()
                lock.release()
                return result
        except Exception as e:
            return e.args[0]
