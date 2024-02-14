import sqlite3
 
class LiteStock:
    def __init__(self):
        self.con = sqlite3.connect("stock.db")
        self.cur = self.con.cursor()
       
    # def select(self):
    #     self.cur.execute("select * from blog")
    #     list = self.cur.fetchall()
    #     ret = []
    #     for e in list:
    #         ret.append({'title':e[0], 'link':e[1], 'description':e[2], 'bloggername':e[3]}
    #                    ,'bloggerlink':e[4], 'postdate':e[5])
    #     return ret
    #
    # def selectOne(self, title):
    #     sql = f"""
    #         select title, link, description, bloggername, bloggerlink, postdate
    #         from blog
    #         where title = '{title}'
    #     """
    #
    #     self.cur.execute(sql)
    #     vo = self.cur.fetchone()
    #     return {'title':vo[0], 'link':vo[1], 'description':vo[2], 'bloggername':vo[3]
    #             , 'bloggerlink':vo[4], 'postdate':vo[5]}
        
    def insert(self, s_id, s_name, price, ymd):
        sql = f"""
            insert into stock
            values
            ("{s_id}","{s_name}","{price}","{ymd}")
            """
            
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def update(self, title, link, description, bloggername, bloggerlink, postdate):
        sql = f"""
            update blog 
            set
            link = '{link}', description='{description}', bloggername='{bloggername}'
                    ,bloggerLink='{bloggerlink}', postdate='{postdate}'
            where title='{title}'
            """
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def delete(self, title):
        sql = f"""
            DELETE FROM blog WHERE title = '{title}'
            """
        self.cur.execute(sql)
        self.con.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def __del__(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    ls = LiteStock()
    # list = le.select()
    # print("list", list)
    # vo = le.selectOne('1')
    # print("vo", vo)
    cnt = ls.insert('3','3','3','3')
    print("cnt", cnt)
    # cnt = le.update('3','6','6','6')
    # print("cnt", cnt)
    # cnt = le.delete('3')
    # print("cnt", cnt)
    