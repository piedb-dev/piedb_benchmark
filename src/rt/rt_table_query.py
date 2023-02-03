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
        c1 = 500000
        c2 = 5000000
        InsertValue().run(c1,c2)
    def insert_500w_1000w(self):
        c1 = 5000000
        c2 = 10000000
        InsertValue().run(c1,c2)

    def parse(self):
        PreTable().run()
        self.insert_0_50w()
        time.sleep(3)
        logger.info("")

        sql = "select * from t;"
        SelectTable().select(sql)

if __name__ == '__main__':
    ta = Table()
    ta.parse()

