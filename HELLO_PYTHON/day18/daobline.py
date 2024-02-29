import oracledb

class DaoBLine:
    def __init__(self):
        oracledb.init_oracle_client() 
        self.con = oracledb.connect(user="python", password="python", dsn="localhost:1521/xe")
        self.cur = self.con.cursor()
        
    
    def near5(self,lng,lat):
        sql = f"""
        select
            bl.bus_id
            ,bl.s_id
            ,bl.s_name
            ,bl.r
            ,bl.lat
            ,bl.lng
        from
            (
            select 
                bus_id
                ,s_id
                ,s_name
                ,SQRT(power(lng-{lng},2)+power(lat-{lat},2)) as r 
                ,lat
                ,lng
            from b_line
            order by r
        )bl
        where
            rownum <= 5
            """
        print("sql",sql)
        
        self.cur.execute(sql)
        list = self.cur.fetchall()
        ret = []
        for e in list:
            ret.append({'bus_id':e[0],'s_id':e[1],'s_name':e[2],'r':e[3],'lat':e[4],'lng':e[5]})
        return ret
    
    
    def getBusIdsBysid(self,s_id):
        sql = f"""
            select bus_id
            from b_line
            where
                s_id = '{s_id}'
        """
        
        self.cur.execute(sql)
        list = self.cur.fetchall()
        ret = []
        for e in list:
            ret.append({'bus_id':e[0]})
        return ret
        
        
    def __del__(self):
        self.cur.close() 
        self.con.close()
    
if __name__ == '__main__':
    dbl = DaoBLine()
    # list = dbl.near5(126.97679444939763,37.57160813833685)
    # print("list",list)
    list = dbl.getBusIdsBysid("01009")
    print("list",list)
    
    
    
    
   