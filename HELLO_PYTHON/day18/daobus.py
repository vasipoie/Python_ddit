import oracledb

class DaoBus:
    def __init__(self):
        oracledb.init_oracle_client() 
        self.con = oracledb.connect(user="python", password="python", dsn="192.168.143.3:1521/xe")
        self.cur = self.con.cursor()
        
    
    def insert(self,bus_id,my_minute):
        sql = f"""
            insert into bus
            (bus_id, eta)
            values 
            ('{bus_id}','{my_minute}')
        """
        
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.rowcount
    
    
        
    def __del__(self):
        self.cur.close() 
        self.con.close()
    
if __name__ == '__main__':
    de = DaoBus()
    cnt = de.insert("1","1")
    print("cnt",cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    