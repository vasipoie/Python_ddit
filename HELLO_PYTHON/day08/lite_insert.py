import sqlite3
 
# SQLite DB 연결
con = sqlite3.connect("python.db")
 
# Connection 으로부터 Cursor 생성
cur = con.cursor()
 
e_id = 4
e_name = 4
gen = 4
addr = 4

sql = f"""
    insert into emp
    values
    ('{e_id}','{e_name}','{gen}','{addr}')
    """
cnt = cur.execute(sql)
con.commit()
print(cur.rowcount)

# Connection 닫기
cur.close()
con.close()