import oracledb

class DaoEmp:
    def __init__(self):
        oracledb.init_oracle_client() 
        self.con = oracledb.connect(user="python", password="python", dsn="localhost:1521/xe")
        self.cur = self.con.cursor()
        
    def select(self):
        self.cur.execute("select * from emp order by e_id")
        list = self.cur.fetchall()
        ret = []
        for e in list:
            ret.append({'e_id':e[0],'e_name':e[1],'gen':e[2],'addr':e[3]})
        return ret
        
    def selectOne(self,e_id):
        sql = f"""
            select 
                e_id,
                e_name,
                gen,
                addr
            from 
                emp
            where
                e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return {'e_id':vo[0],'e_name':vo[1],'gen':vo[2],'addr':vo[3]}
    
    def insert(self,e_id,e_name,gen,addr):
        sql = f"""
            insert into emp
            (e_id, e_name, gen, addr)
            values 
            ('{e_id}','{e_name}','{gen}','{addr}')
        """
        
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.rowcount
    
    def update(self,e_id,e_name,gen,addr):
        sql = f"""
            update emp
            set 
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            where
                e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.rowcount
    
    def delete(self,e_id):
        sql = f"""
            delete from emp
            where
                e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.rowcount
        
    def __del__(self):
        self.cur.close() 
        self.con.close()
    
if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.delete("3")
    print("cnt",cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    