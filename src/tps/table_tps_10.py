# -- coding: utf-8 --
# @Time : 2023/2/1  10:31
# @Author : wangdexin
# @File : table_tps_10.py
# -- coding: utf-8 --
# @Time : 2023/1/31  10:49
# @Author : wangdexin
# @File : table_tps_1.py.py
import time,re,psycopg2
from tools import get_hardware_info
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
        for step in range(1,100000,10):
            li = []
            for j in range(step,step+10):
                vv = '''({},{},{},'测试','测试二')'''.format(j,j,j)
                li.append(vv)
            v = ','.join(li)
            sql = '''insert into t values {};'''.format(v)
            cursor.execute(sql)
        t2 = time.time()
        inter = t2-t1
        print(inter)
        tps = 100000/inter
        print('tps = {}'.format(tps))
    def create_table(self):
        sql = '''create table t (id int,v1 int,v2 int,s1 varchar,s2 varchar);'''
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
