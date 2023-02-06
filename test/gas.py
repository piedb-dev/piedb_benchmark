# -- coding: utf-8 --
# @Time : 2023/2/6  15:44
# @Author : wangdexin
# @File : gas.py

import json, sys, time, random
from kafka import KafkaProducer

host_list = ['A','B','C','D','E']
blast_furnace_list = [1,2,3,4,5,6,7,8]
detector_list = [0,1,2,3,4,5,6,7,8,9]

class Kafka(object):
    def __init__(self):
        pass
    def parse(self, kafkaTopic):
        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
        cur = 10000000
        while True:
            # time.sleep(0.4)
            for i in blast_furnace_list:
                for j in host_list:
                    json_object = {}
                    for ids in detector_list:
                        now = int(round(time.time() * 1000))
                        date_v = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
                        cur = cur+1
                        value = random.randint(1, 2000)
                        if value % 100 == 0:
                            value = -999
                        json_object['auto_id'] = cur
                        json_object['host_id'] = j
                        json_object['blast_furnace_id'] = i
                        json_object['datector_type'] = 1
                        json_object['detector_id'] = str(i)+j+"-{}".format(str(ids))
                        json_object['concentration'] = value
                        json_object['time_point'] = date_v
                        # json_object['update_time'] = now
                        # print(json_object)
                        value = json.dumps(json_object)
                        try:
                            producer.send(
                                kafkaTopic,
                                key=str(json_object["time_point"]).encode("utf8"),
                                value=value.encode("utf-8"),
                            )

                            if cur % 10000 == 0:
                                print("count = %d" % i)
                        except Exception as e:
                            print(str(e))

if __name__ == '__main__':
    kafka = Kafka()
    kafkaTopic = sys.argv[1]
    kafka.parse(kafkaTopic)


