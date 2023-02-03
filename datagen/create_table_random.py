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
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def run(self,c1,c2):
        self.parse(c1,c2)
        self.conn.close()


class PreTable(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            database="dev",
            user="root",
            host="127.0.0.1",
            port=5505
        )
    def create_table(self):
        sql = '''create table t (id int primary key,uid int,v1 int,v2 float,s1 varchar,s2 varchar,update_time timestamp);'''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def create_index(self):
        sql = '''create index uid_i on t(uid);'''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def delete_table(self):
        try:
            sql = '''drop table t;'''
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()

        except:
            pass
    def delete_index(self):
        try:
            sql = '''drop index uid_i;'''
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except:
            pass

    def run(self):
        self.delete_index()
        self.delete_table()
        self.create_table()
        self.create_index()

class SelectTable(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            database="dev",
            user="root",
            host="127.0.0.1",
            port=5505
        )

    def select(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        nums = cursor.fetchall()
        return nums






