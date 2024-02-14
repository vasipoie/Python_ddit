import oracledb

class DaoEmp:
    def __init__(self):
        oracledb.init_oracle_client()
        self.con = oracledb.connect(user="python", password="python", dsn="localhost:1521/xe")   # DB에 연결 (호스트이름 대신 IP주소 가능)
        self.cur = self.con.cursor()   # 연결된 DB 지시자(커서) 생성
       
    def select(self):
        self.cur.execute("select * from emp order by e_id")
        list = self.cur.fetchall()
        ret = []
        for e in list:
            ret.append({'e_id':e[0], 'e_name':e[1], 'gen':e[2], 'addr':e[3]})
        return ret
    
    def selectOne(self, e_id):
        sql = f"""
            select e_id, e_name, gen, addr
            from emp
            where e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return {'e_id':vo[0], 'e_name':vo[1], 'gen':vo[2], 'addr':vo[3]}
        
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
            insert into emp
            values
            ('{e_id}','{e_name}','{gen}','{addr}')
            """
            
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        sql = f"""
            update emp 
            set
            e_name = '{e_name}', gen='{gen}', addr='{addr}'
            where e_id='{e_id}'
            """
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            DELETE FROM emp WHERE e_id = '{e_id}'
            """
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def __del__(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    de = DaoEmp()
    list = de.select()
    print("list", list)
    vo = de.selectOne('1')
    print("vo", vo)
    # cnt = de.insert('3','3','3','3')
    # print("cnt", cnt)
    cnt = de.update('3','6','6','6')
    print("cnt", cnt)
    cnt = de.delete('3')
    print("cnt", cnt)
    