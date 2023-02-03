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

class Table(object):
    def __init__(self):
        pass
    def insert_0_50w(self):
        logger.info("Writing 50w data！！! please waiting....")
        c1 = 0
        c2 = 500000
        InsertValue().run(c1,c2)
    def insert_50w_500w(self):
        logger.info("Writing 500w data！！! please waiting....")
        c1 = 500000
        c2 = 5000000
        InsertValue().run(c1,c2)
    def insert_500w_1000w(self):
        logger.info("Writing 1000w data！！! please waiting....")
        c1 = 5000000
        c2 = 10000000
        InsertValue().run(c1,c2)

    def parse(self):
        PreTable().run()
        self.insert_0_50w()
        time.sleep(3)
        sql_pointget_pk = 'select * from t where id = 10000;'
        sql_pointget_index = 'select * from t where uid = 10000;'
        sql_pointget_normal = 'select * from t where v1 = 10000;'

        sql_scan_pk = 'select * from t where id < 10000 and id > 0;'
        sql_scan_index = 'select * from t where id < 10000 and id > 0;'
        sql_scan_normal = 'select * from t where id < 10000 and id > 0;'
        conn = SelectTable()
        conn.select(sql_pointget_pk)
        conn.select(sql_pointget_index)
        conn.select(sql_pointget_normal)
        conn.select(sql_scan_pk)
        conn.select(sql_scan_index)
        conn.select(sql_scan_normal)


if __name__ == '__main__':
    ta = Table()
    ta.parse()

