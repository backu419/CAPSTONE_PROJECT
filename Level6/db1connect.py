import sqlite3


class SearchDB():

    def __init__(self):
        self.connect = sqlite3.connect("C://sqlite//hcl.db")
        self.cur = self.connect.cursor()

    def SearcDB(self, fil):


        # self.connect = sqlite3.connect("C://sqlite//hcl.db")
        # self.cur = self.connect.cursor()
        sql = """select * from filelog where filename 'like%{0}'""".format(fil)
        # args = (filename,)
        # self.cur.execute(sql,args)
        # row=self.cur.fetchone()
        # print(row)

        self.cur.execute(sql)
        row = self.cur.fetchone()

        if row==None:
            return 0
        else:
            return row

    def insertDB(self, filename):
        sql = """insert into filelog(filename) values(?);"""

        data = (filename,)

        self.cur.execute(sql, data)
        self.connect.commit()
        return "Record Added"


if __name__ == '__main__':
    obj = SearchDB()
    print(obj.connect)
    print(obj.cur)
    # obj.SearcDB()
