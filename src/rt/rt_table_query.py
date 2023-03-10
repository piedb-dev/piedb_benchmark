# -- coding: utf-8 --
# @Time : 2023/2/2  17:32
# @Author : wangdexin
# @File : rt_table_query.py
import psycopg2,time,datetime,random,os,sys,logging
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from datagen.create_table_random import PreTable,InsertValue,SelectTable
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from sql.sql import select_table_scan,select_table_pointget
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

    def parse_50w(self):
        PreTable().run()
        self.insert_0_50w()
        time.sleep(3)
        ii = 0
        while ii<5:
            logger.info("50w data,{} !!!!".format(ii))
            ii+=1
            key = random.randint(1,500000)
            conn = SelectTable()
            for sq in select_table_pointget:
                sql = sq.format(key)
                conn.select(sql)

            key_scan = random.randint(1,490000)
            for sq in select_table_scan:
                sql = sq.format(key_scan,key_scan+10000)
                conn.select(sql)
    def parse_100w(self):
        self.insert_50w_100w()
        time.sleep(5)
        ii = 0
        while ii<5:
            logger.info("100w data,{} !!!!".format(ii))
            ii+=1
            key = random.randint(1,1000000)
            conn = SelectTable()
            for sq in select_table_pointget:
                sql = sq.format(key)
                conn.select(sql)

            key_scan = random.randint(1,990000)
            for sq in select_table_scan:
                sql = sq.format(key_scan,key_scan+10000)
                conn.select(sql)

    def parse_1000w(self):
        self.insert_500w_1000w()
        time.sleep(10)
        ii = 0
        while ii<5:
            logger.info("1000w data,{} !!!!".format(ii))
            ii+=1
            key = random.randint(1,10000000)
            conn = SelectTable()
            for sq in select_table_pointget:
                sql = sq.format(key)
                conn.select(sql)

            key_scan = random.randint(1,99990000)
            for sq in select_table_scan:
                sql = sq.format(key_scan,key_scan+10000)
                conn.select(sql)

if __name__ == '__main__':
    ta = Table()
    ta.parse_50w()
    ta.parse_100w()
    # ta.parse_1000w()


