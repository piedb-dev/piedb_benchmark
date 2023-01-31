# -- coding: utf-8 --
# @Time : 2023/1/31  10:24
# @Author : wangdexin
# @File : get_info.py.py
from subprocess import Popen, PIPE
import json
import time

def run_command(command,flag = True):
    process = Popen(command,shell=flag,stdout=PIPE,stderr=PIPE)
    stdout,stderr = process.communicate()
    return str(stdout,encoding='utf-8')

def get_os_info():
    model = run_command("dmidecode -s system-product-name | awk '{printf(\"%s\",$0)}'")
    cpuNum = run_command("cat /proc/cpuinfo | grep 'cpu cores' | uniq | cut -d: -f2| awk '{printf(\"%s\",$0)}'")
    diskSize = run_command("/opt/MegaRAID/MegaCli/MegaCli64 -PDlist -aALL -NoLog| grep 'Raw Size' | awk '{print $3}' | awk 'BEGIN{i=1} {while(i<NF) print NF,$i,i++}{sum = int($i*1024*1024*1024/1000/1000/1000)}{u += sum}END{printf u\"T\"}'")
    memNum = run_command("dmidecode|grep -P -A5 'Memory\s+Device'| grep Size | grep -v Range |grep -v No | wc -l | awk '{printf(\"%s\",$0)}'")
    output = [{
        "model": model,
        "cpuNum": cpuNum,
        "diskSize": diskSize,
        "memNum": memNum
    }]
    return output
a = get_os_info()
print(a)