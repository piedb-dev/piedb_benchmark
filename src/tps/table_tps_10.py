# -- coding: utf-8 --
# @Time : 2023/2/1  10:31
# @Author : wangdexin
# @File : table_tps_10.py

import time,re,psycopg2,datetime,random
class Test(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            database="dev",
            user="root",
            host="127.0.0.1",
            port=5505
        )

    def parse(self):
        t1 = time.time()
        cursor = self.conn.cursor()
        for step in range(1,1000000,10):
            li = []
            for j in range(step,step+10):
                v2 = random.uniform(1, 1000)
                update_time = datetime.datetime.now()
                vv = '''({},{},{},{},'test1','test2','{}')'''.format(j,j,j,v2,update_time)
                li.append(vv)
            v = ','.join(li)
            sql = '''insert into t values {};'''.format(v)
            cursor.execute(sql)
        t2 = time.time()
        inter = t2-t1
        print(inter)
        tps = 1000000/inter
        print('tps = {}'.format(tps))
    def create_table(self):
        sql = '''create table t (id int,uid int,v1 int,v2 float,s1 varchar,s2 varchar,update_time timestamp);'''
        cursor = self.conn.cursor()
        cursor.execute(sql)

    def delete_table(self):
        try:
            sql = '''drop table t;'''
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except:
            pass

    def run(self):
        self.delete_table()
        self.create_table()
        self.parse()
        self.conn.close()

if __name__ == '__main__':
    test = Test()
    test.run()
