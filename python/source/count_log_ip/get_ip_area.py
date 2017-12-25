"""
python版本:3.6.1
获取指定IP的地理位置
使用方法 python get_ip_area.py ip
"""
#!/usr/bin/env python
#coding:utf-8

try:
    import sys,json
    from urllib import request
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % sys.argv[1] 
    content = request.urlopen(apiurl)
    htmls = content.read()
    htmls = str(htmls,encoding='utf-8')
    data = json.loads(htmls)['data']      #强制转换化json
    code = json.loads(htmls)['code']

    print(data)
    if code == 0:
        #print(data['country']+data['region']+data['city']+data['东北']+data['city'])
        #print(data['country_id'])
        show = data['country'] + data['region'] + data['city'] + data['area'] + data['isp']
        print(show)
        #print(data['region'])
    else:
        print(data)
except:
    print("Usage:%s IP" % sys.argv[0])