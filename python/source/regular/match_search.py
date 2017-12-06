'''
10-13 search与match函数

findall #可以匹配到多次
#下面两函数,仅匹配到一次
re.match  #尝试从字符的首位开始匹配,只要匹配不到.就会返回None
re.search #尝试全部匹配后,才返回结果
'''

import re


s = 'A3C72D1D8E67'
r = re.match('\d',s)
print(r) # 输出:None

s = '83C72D1D8E67'

r = re.match('\d',s)
print(r) # 输出: <_sre.SRE_Match object; span=(0, 1), match='8'>

r = re.search('\d',s)
print(r) # 输出: <_sre.SRE_Match object; span=(0, 1), match='8'>

'''
r.span()  #返回匹配到的位置
r.group() #返回对象的结果
'''
s = 'A3C72D1D8E67'
r = re.search('\d',s)
print(r.group()) # 输出: 3
print(r.span()) # 输出: (1, 2)




