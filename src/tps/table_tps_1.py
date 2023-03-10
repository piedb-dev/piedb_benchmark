# -- coding: utf-8 --
# @Time : 2023/1/31  10:49
# @Author : wangdexin
# @File : table_tps_1.py.py
import time,re,psycopg2
import random,datetime
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
        for i in range(1,100000):
            v2 = random.uniform(1, 1000)
            update_time = datetime.datetime.now()
            sql = '''insert into t values({},{},{},{},'test1','test2','{}');'''.format(i,i,i,v2,update_time)
            cursor.execute(sql)
        t2 = time.time()
        inter = t2-t1
        print(inter)
        tps = 100000/inter
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
