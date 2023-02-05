# -- coding: utf-8 --
# @Time : 2023/2/3  19:37
# @Author : wangdexin
# @File : rt_materialized_view_query.py

import psycopg2,time,datetime,random,os,sys,logging
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from datagen.create_table_random import PreTable,InsertValue,SelectTable
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from sql.sql import select_view_scan,select_view_pointget

class View(object):
    def __init__(self):
        pass

    def parse(self):
        ii = 0
        while ii<5:
            logger.info("500w data source,{} !!!!".format(ii))
            ii+=1
            key = random.randint(0,10000000)
            conn = SelectTable()
            for sq in select_view_pointget:
                sql = sq.format(key)
                conn.select(sql)

            key_scan = random.randint(0,9990000)
            for sq in select_view_scan:
                sql = sq.format(key_scan,key_scan+10000)
                conn.select(sql)

if __name__ == '__main__':
    ta = View()
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


create materialized view mv1 as 
    select id,max(uid) as uid_max,max(v1) as v1_max,time_point from s1 
group by id,time_point;
'''


