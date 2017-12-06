'''
10-10 匹配模式参数

re.findall的第三个参数

忽略大小写
import re

re.findall('c#',lanuage,re.I)  

使用多个模式 |线来区分
re.findall('c#',lanuage,re.I | re.S) 

re.I  #不区分大小写
re.S  #表匹配除换行符\n之外其它所有字符

'''

import re

language = 'PythonC#JavaPHP'
r = re.findall('c#',language)
print(r)     # 输出: []


r = re.findall('c#',language,re.I | re.S)
print(r)     # 输出:['C#']


language = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}',language,re.I)
print(r)     # 输出:[]

language = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}',language,re.I | re.S)
print(r)     # 输出:['C#\n']