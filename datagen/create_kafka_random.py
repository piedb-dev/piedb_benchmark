# -- coding: utf-8 --
# @Time : 2023/2/3  19:11
# @Author : wangdexin
# @File : create_kafka_random.py

import json, sys, time, random,datetime
from kafka import KafkaProducer
class Kafka(object):
    def __init__(self):
        pass
    def parse(self, kafkaTopic):
        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
        cur = 0
        while cur < 500000:
            json_object = {}
            cur = cur+1
            v2 = random.uniform(1, 1000)
            update_time = datetime.datetime.now()
            now = int(round(time.time() * 1000))
            date_v = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))

            json_object['id'] = cur
            json_object['uid'] = cur
            json_object['v1'] = cur
            json_object['v2'] = v2
            json_object['s1'] = 'test1'
            json_object['s2'] = 'test2'
            json_object['time_point'] = date_v
            value = json.dumps(json_object)
            try:
                producer.send(
                    kafkaTopic,
                    key=str(json_object["time_point"]).encode("utf8"),
                    value=value.encode("utf-8"),
                )
                if cur % 10000 == 0:
                    print("cur = %d" % cur)
            except Exception as e:
                print(str(e))

if __name__ == '__main__':
    kafka = Kafka()
    kafkaTopic = sys.argv[1]
    kafka.parse(kafkaTopic)

