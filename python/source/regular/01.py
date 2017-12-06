"""
10-7 匹配0次1次或者无限多次

*  #匹配0次或者无限多次
+  #匹配1次或者无限多次
?  #匹配0次或者1次
"""

import re
a = 'python)python1pythonn2'

r = re.findall('python*',a)
print(r)  #输出: ['python', 'python', 'pythonn']

r = re.findall('python+',a) 
print(r)  #输出: ['python', 'python', 'pythonn']


r = re.findall('python?',a)  
print(r) #输出: ['python', 'python', 'python']

## 贪婪及非贪婪 
r = re.findall('python{1,2}',a)  
print(r) #输出:['python', 'python', 'pythonn']


r = re.findall('python{1,2}?',a)  
print(r) #输出: ['python', 'python', 'python']