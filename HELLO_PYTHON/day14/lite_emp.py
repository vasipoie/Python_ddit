import sqlite3
 
class LiteEmp:
    def __init__(self):
        self.con = sqlite3.connect("crawl.db")
        self.cur = self.con.cursor()
       
    def select(self):
        self.cur.execute("select * from emp")
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
    le = LiteEmp()
    # list = le.select()
    # print("list", list)
    # vo = le.selectOne('1')
    # print("vo", vo)
    cnt = le.insert('3','3','3','3')
    print("cnt", cnt)
    # cnt = le.update('3','6','6','6')
    # print("cnt", cnt)
    # cnt = le.delete('3')
    # print("cnt", cnt)
    