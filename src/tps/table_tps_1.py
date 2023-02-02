# -- coding: utf-8 --
# @Time : 2023/1/31  10:49
# @Author : wangdexin
# @File : table_tps_1.py.py
import time,re,psycopg2
from tools import get_hardware_info
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
        for i in range(1,10000):
            v2 = random.uniform(1, 1000)
            t1 = datetime.datetime.now()
            sql = '''insert into t values({},{},{},{},'test1','test2','{}');'''.format(i,i,i,v2,t1)
            cursor.execute(sql)
        t2 = time.time()
        inter = t2-t1
        print(inter)
        tps = 10000/inter
        print('tps = {}'.format(tps))
    def create_table(self):
        sql = '''create table t (id int,uid int,v1 int,v2 float,s1 varchar,s2 varchar,t1 timestamp);'''
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
        get_hardware_info.get_os_info()
        self.delete_table()
        self.create_table()
        self.parse()
        self.conn.close()

if __name__ == '__main__':
    test = Test()
    test.run()
