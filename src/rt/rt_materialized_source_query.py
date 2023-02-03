# -- coding: utf-8 --
# @Time : 2023/2/3  16:35
# @Author : wangdexin
# @File : rt_source_query.py

import psycopg2,time,datetime,random,os,sys,logging
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from datagen.create_table_random import PreTable,InsertValue,SelectTable
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from sql.sql import select_source_pointget,select_source_scan
class Table(object):
    def __init__(self):
        pass
    def insert_0_50w(self):
        logger.info("Writing 50w data！！! please waiting....")
        c1 = 0
        c2 = 500000
        InsertValue().run(c1,c2)
    def insert_50w_100w(self):
        logger.info("Writing 500w data！！! please waiting....")
        c1 = 500000
        c2 = 1000000
        InsertValue().run(c1,c2)
    def insert_500w_1000w(self):
        logger.info("Writing 1000w data！！! please waiting....")
        c1 = 5000000
        c2 = 10000000
        InsertValue().run(c1,c2)

    def parse(self):
        ii = 0
        while ii<5:
            logger.info("50w data source,{} !!!!".format(ii))
            ii+=1
            key = random.randint(1,500000)
            conn = SelectTable()
            for sq in select_source_pointget:
                sql = sq.format(key)
                conn.select(sql)

            key_scan = random.randint(1,490000)
            for sq in select_source_scan:
                sql = sq.format(key_scan,key_scan+10000)
                conn.select(sql)

if __name__ == '__main__':
    ta = Table()
    ta.parse()



'''
create materialized source s1 (
    id int PRIMARY KEY,
    uid int,
    v1 int,
    v2 float,
    s1 varchar,
    s2 varchar,
    time_point timestamp
) with (
  connector = 'kafka',
  topic = 'test',
  properties.bootstrap.server = 'kafka:9092',
  scan.startup.mode = 'earliest'
) row format json;
'''

