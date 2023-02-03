# -- coding: utf-8 --
# @Time : 2023/2/1  15:31
# @Author : wangdexin
# @File : __init__.py.py

import psycopg2,time,json
from psycopg2.extras import LoggingConnection, LoggingCursor

class Piedb(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            database="dev",
            user="root",
            host="127.0.0.1",
            port=5505
        )
    def get_connecttion(self):
        return self.conn


class MyLoggingCursor(LoggingCursor):
    def execute(self, query, vars=None):
        self.timestamp = time.time()
        return super(MyLoggingCursor, self).execute(query, vars)

    def callproc(self, procname, vars=None):
        self.timestamp = time.time()
        return super(MyLoggingCursor, self).callproc(procname, vars)

class MyLoggingConnection(LoggingConnection):
    def filter(self, msg, curs):
        interal = int((time.time() - curs.timestamp) * 1000)
        return str(msg,encoding='utf-8') + "   {} ms".format(interal)

    def cursor(self, *args, **kwargs):
        kwargs.setdefault('cursor_factory', MyLoggingCursor)
        return LoggingConnection.cursor(self, *args, **kwargs)



