'''
python版本:3.6.1
1.对/var/log/nginx/access.log的ip进行分组统计并且排序
2.加入IP地址地理查询及限制输出多少条

使用方法:
     python count.py
     python count.py log 1 #查看日志前1条
     python count.py log 2 #查看日志前2条
     python count.py log 3 #查看日志前3条
'''

import re
import sys
from fn_get_ip_area import get_ip_area

fp = open("./log2.txt",'r')

#print(type(sys.argv[1]))

try:
    param_log = sys.argv[1]
    param_num = int(sys.argv[2])
except:
    param_log = 0
    param_num = 0


arr = {}      #用字典来存储IP跟访问次数
count = 0 
for s in fp.readlines():
    ip = re.findall('((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))',s)
   # print(ip[0][0])
    _ip = ip[0][0]
    if _ip in set(k.lower() for k in arr):
        arr[_ip] += 1
    else:
        arr[_ip]=1
fp.close()

#print(arr)


#排序输出
numberlist = list(set(arr.values()))    #set集合这里是去重
numberlist.sort(reverse=True)           #reverse=True表示逆序，reverse=False表示顺序

i=1
for ipNum in numberlist:
    for ip in arr:
        if(ipNum == arr[ip]):
            if param_log and i<=param_num:
                i+=1
                print(ip + "  --->" + str(arr[ip]) + '  地址:' +get_ip_area(ip))
            else:
                print(ip + "  --->" + str(arr[ip]))

"""
输出:
211.140.222.131--->71
182.138.143.150--->67
123.60.101.17--->53
106.6.61.226--->44
175.20.88.200--->32
124.67.136.122--->28
113.104.166.177--->26
121.34.154.205--->24
220.160.55.184--->20
23.105.74.106--->19
101.254.208.100--->18
175.20.88.203--->11
119.57.159.183--->10
111.206.36.135--->10
175.20.88.205--->9
175.20.88.201--->8
119.57.159.181--->8
119.57.159.182--->8
119.57.159.184--->8
220.181.125.178--->8
119.57.159.180--->8
175.20.88.204--->8
"""            

