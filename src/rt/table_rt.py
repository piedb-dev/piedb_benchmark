# -- coding: utf-8 --
# @Time : 2023/2/2  16:23
# @Author : wangdexin
# @File : table_rt.py
import psycopg2,time,datetime,random,os,sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from datagen.create_table_random import InsertValue


class Table_RT(object):



    def __init__(self):
        self.conn = psycopg2.connect(
            database="dev",
            user="root",
            host="127.0.0.1",
            port=5505
        )
    def parse(self):
        c1 = 0
        c2 = 1000
        InsertValue().run(c1,c2)
    def create_table(self):
        sql = '''create table t (id int primary key,uid int,v1 int,v2 float,s1 varchar,s2 varchar,update_time timestamp);'''
        cursor = self.conn.cursor()
        cursor.execute(sql)
    def create_index(self):
        sql = '''create index uid_i on t(uid);'''
        cursor = self.conn.cursor()
        cursor.execute(sql)

    def delete_table(self):
        try:
            sql = '''drop table t;'''
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except:
            pass
    def delete_index(self):
        try:
            sql = '''drop index uid_i;'''
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except:
            pass
    def run(self):
        self.delete_index()
        self.delete_table()
        self.create_table()
        self.create_index()
        self.parse()
if __name__ == '__main__':
    table = Table_RT()
    table.run()


