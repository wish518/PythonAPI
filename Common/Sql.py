import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    user="wish",
    password="XXXXX",
    db="dtw",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
class sql: 
    # 使用pymysql指令來連接數據庫
    def GetDataRow(self, sqlStr,parms):
        try:
            connection.connect()
            # 從數據庫鏈接中得到cursor的數據結構
            with connection.cursor() as cursor:
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
                connection.commit()
                # 關閉 SQL 連線
                connection.close()
                return result
        except Exception as e:
            return e.args[0]
            
    # 使用pymysql指令來連接數據庫
    def GetDataTable(self, sqlStr,parms):
        try:
            # 從數據庫鏈接中得到cursor的數據結構
            connection.connect()
            with connection.cursor() as cursor:
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
                connection.commit()
                # 關閉 SQL 連線
                connection.close()
                return result
        except Exception as e:
            return e.args[0]
