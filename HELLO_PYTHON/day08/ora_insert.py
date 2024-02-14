import oracledb

oracledb.init_oracle_client()
con = oracledb.connect(user="python", password="python", dsn="localhost:1521/xe")   # DB에 연결 (호스트이름 대신 IP주소 가능)
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

# cur.execute("insert into emp values (3,'3','3','3')")
con.commit()
print(cur.rowcount)

cur.execute("select * from emp")
rows = cur.fetchall()
print(rows)