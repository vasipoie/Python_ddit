import oracledb

oracledb.init_oracle_client()
con = oracledb.connect(user="python", password="python", dsn="localhost:1521/xe")   # DB에 연결 (호스트이름 대신 IP주소 가능)
cur = con.cursor()   # 연결된 DB 지시자(커서) 생성

# for row in cur.execute("select * from emp"):
#     print(row)
    
cur.execute("select * from emp")
rows = cur.fetchall()
print(rows)
    
# cur.execute("select * from emp")
# out_data = cur.fetchone()
# print("=====>", out_data[0])

cur.close()
con.close()
    
# cur.execute("select * from emp") # 데이터베이스 명령 실행( cursor가 임시로 보관)
# out_data = cur.fetchall() # 커서의 내용을 out_data에 저장 
# for record in out_data: # out_data의 내용을 출력
#     print(record)