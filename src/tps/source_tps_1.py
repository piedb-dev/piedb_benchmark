# -- coding: utf-8 --
# @Time : 2023/1/31  10:50
# @Author : wangdexin
# @File : source_tps_1.py

import time, re, psycopg2
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
        time.sleep(3)
        sql = '''select count(*) from s1;'''
        cursor.execute(sql)
        nums = cursor.fetchall()[0][0]
        print(nums)
        t2 = time.time()
        inter = t2 - t1
        print(inter)
        tps = nums / inter
        print('tps = {}'.format(tps))

    def create_source(self):
        sql = '''
        create materialized source s1 (
            auto_id int PRIMARY KEY,
            auto_index int,
            host_id varchar,
            blast_furnace_id int,
            detector_type int,
            detector_id varchar,
            concentration int,
            time_point timestamp
        ) with (
              connector = 'kafka',
              topic = 'record',
              properties.bootstrap.server = 'kafka:9092',
              scan.startup.mode = 'earliest'
        ) row format json;'''

        cursor = self.conn.cursor()
        cursor.execute(sql)

    def delete_source(self):
        try:
            sql = '''drop source s1;'''
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except:
            pass

    def run(self):
        get_hardware_info.get_os_info()
        self.delete_source()
        self.create_source()
        self.parse()
        self.conn.close()


if __name__ == '__main__':
    test = Test()
    test.run()





