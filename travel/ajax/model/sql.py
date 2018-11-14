import pymysql

class sql():
    def __init__(self):
        self.db=pymysql.connect('localhost','root','113206','travel',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
        self.cursor=self.db.cursor()
    def one(self,str,*args):
        self.cursor.execute(str,*args)
        id=self.db.insert_id()
        self.db.commit()
        return id
    def many(self,str,*args):
        self.cursor.executemany(str,*args)
        self.db.commit()
    def sel_one(self,str,*args):
        self.cursor.execute(str,*args)
        data=self.cursor.fetchone()
        return data
    def sel_many(self,str,*args):
        self.cursor.execute(str,*args)
        data=self.cursor.fetchall()
        return data
    def close(self):
        self.cursor.close()
        self.db.close()