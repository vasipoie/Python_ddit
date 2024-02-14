import oracledb

class DaoMem:
    def __init__(self):
        oracledb.init_oracle_client()
        self.con = oracledb.connect(user="python", password="python", dsn="localhost:1521/xe")   # DB에 연결 (호스트이름 대신 IP주소 가능)
        self.cur = self.con.cursor()   # 연결된 DB 지시자(커서) 생성
       
    def select(self):
        self.cur.execute("select * from mem")
        list = self.cur.fetchall()
        ret = []
        for m in list:
            ret.append({'m_id':m[0], 'm_name':m[1], 'tel':m[2], 'email':m[3]})
        return ret
    
    def selectOne(self, m_id):
        sql = f"""
            select m_id, m_name, tel, email
            from mem
            where m_id = '{m_id}'
        """
        
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return {'m_id':vo[0], 'm_name':vo[1], 'tel':vo[2], 'email':vo[3]}
        
    def insert(self, m_id, m_name, tel, email):
        sql = f"""
            insert into mem
            values
            ('{m_id}','{m_name}','{tel}','{email}')
            """
            
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def update(self, m_id, m_name, tel, email):
        sql = f"""
            update mem 
            set
            m_name = '{m_name}', tel='{tel}', email='{email}'
            where m_id='{m_id}'
            """
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def delete(self, m_id):
        sql = f"""
            DELETE FROM mem WHERE m_id = '{m_id}'
            """
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def __del__(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    de = DaoMem()
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
    