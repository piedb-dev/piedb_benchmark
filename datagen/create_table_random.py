# -- coding: utf-8 --
# @Time : 2023/2/2  11:11
# @Author : wangdexin
# @File : create_table_1000.py

import psycopg2,random,datetime
class InsertValue(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            database="dev",
            user="root",
            host="127.0.0.1",
            port=5505
        )

    def parse(self,c1,c2):
        cursor = self.conn.cursor()
        for step in range(c1,c2,20):
            li = []
            for j in range(step,step+20):
                v2 = random.uniform(1, 1000)
                update_time = datetime.datetime.now()
                vv = '''({},{},{},{},'test1','test2','{}')'''.format(j,j,j,v2,update_time)
                li.append(vv)
            v = ','.join(li)
            sql = '''insert into t values {};'''.format(v)
            cursor.execute(sql)
    def run(self,c1,c2):
        self.parse(c1,c2)
        self.conn.close()

if __name__ == '__main__':
    test = InsertValue()
    c1 = 0
    c2 = 100
    test.run(c1,c2)
