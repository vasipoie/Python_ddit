import sqlite3
 
# SQLite DB 연결
con = sqlite3.connect("python.db")
 
# Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# SQL 쿼리 실행
cur.execute("select * from emp")
 
# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
    print(row)
 
# Connection 닫기
cur.close()
con.close()