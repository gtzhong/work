"""
python版本:3.6.1
获取指定IP的地理位置
使用方法 
"""

import sys,json
import time
from urllib import request

def get_ip_area(ip):
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip 
        content = request.urlopen(apiurl)
        htmls = content.read()
        htmls = str(htmls,encoding='utf-8')
        data = json.loads(htmls)['data']      #强制转换化json
        code = json.loads(htmls)['code']
        if code == 0:
            time.sleep(0.1)
            show = data['country'] + data['region'] + data['city'] + data['area'] + data['isp']
            return show
    except:
        return '查不到'