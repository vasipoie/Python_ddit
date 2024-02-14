import sqlite3
 
# SQLite DB 연결
con = sqlite3.connect("python.db")
 
# Connection 으로부터 Cursor 생성
cur = con.cursor()
 
e_id = 4
e_name = 6
gen = 6
addr = 6

sql = f"""
    DELETE FROM emp WHERE e_id = '{e_id}'
    """
cnt = cur.execute(sql)
con.commit()
print(cur.rowcount)

# Connection 닫기
cur.close()
con.close()