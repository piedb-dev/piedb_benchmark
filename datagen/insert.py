# -- coding: utf-8 --
# @Time : 2023/2/3  17:11
# @Author : wangdexin
# @File : insert.py
import time,random,datetime
import psycopg2

class Insert(object):
    def __init__(self):
        conn = psycopg2.connect(
            database="dev",
            user="root",
            host="localhost",
            port=5505
        )
        self.cursor = conn.cursor()

    def parse(self):
        for step in range(1,5000000,10):
            li = []
            for j in range(step,step+10):
                v2 = random.uniform(1, 1000)
                update_time = datetime.datetime.now()
                vv = '''({},{},{},{},'test1','test2','{}')'''.format(j,j,j,v2,update_time)
                li.append(vv)
            v = ','.join(li)
            sql = '''insert into t values {};'''.format(v)
            self.cursor.execute(sql)

    def run(self):
        self.parse()
if __name__ == '__main__':
    ins = Insert()
    ins.run()
