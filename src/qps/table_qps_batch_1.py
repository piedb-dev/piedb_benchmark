import time,re,psycopg2
'''
create table t (id int,v1 int,v2 int,s1 varchar,s2 varchar);
'''
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
        for i in range(1,10000):
            sql = '''insert into t values({},{},{},'测试','测试二');'''.format(i,i,i)
            cursor.execute(sql)
        t2 = time.time()
        inter = t2-t1
        print(inter)
        tps = 10000/inter
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
        self.delete_table()
        self.create_table()
        self.parse()
        self.conn.close()
if __name__ == '__main__':
    test = Test()
    test.run()