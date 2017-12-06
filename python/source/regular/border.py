'''
10-8 边界匹配符

^xxxx$
'''

import re

qq ='100001'
r = re.findall('\d{4,8}',qq)
print(r) # 输出 :['100001']

qq ='101'
r = re.findall('\d{4,8}',qq)
print(r) # 输出 :[]


qq ='1000000001'
r = re.findall('\d{4,8}',qq)
print(r) # 输出 :['10000000']

r = re.findall('000',qq)
print(r) # 输出 :['000', '000']

r = re.findall('000$',qq)
print(r) # 输出 :[]

