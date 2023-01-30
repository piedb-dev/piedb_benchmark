import time,re,psycopg2,threading
maxThread = 10
sem = threading.BoundedSemaphore(maxThread)
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
        self.cursor = self.conn.cursor()

    def parse(self,cur):
        for i in range(cur,cur+10000):
            sql = '''insert into t values({},{},{},'测试','测试二');'''.format(i,i,i)
            self.cursor.execute(sql)
        sem.release()

    def create_table(self):
        sql = '''create table t (id int,v1 int,v2 int,s1 varchar,s2 varchar);'''
        cursor = self.conn.cursor()
        cursor.execute(sql)

    def delete_table(self):
        sql = '''drop table t;'''
        cursor = self.conn.cursor()
        cursor.execute(sql)

    def thread(self):
        for i in range(0,100000,10000):
            sem.acquire()
            task = threading.Thread(target=self.parse,args=(i,))
            task.start()
        task.join()


    def run(self):
        self.delete_table()
        self.create_table()
        t1 = time.time()
        self.thread()
        t2 = time.time()
        inter = t2 - t1
        print(inter)
        tps = 100000 / inter
        print(tps)
        #self.conn.close()
if __name__ == '__main__':
    test = Test()
    test.run()