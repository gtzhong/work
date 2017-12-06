"""
10-5 数量词
[a-z]{3}
[a-z]{3,6}
"""

import re
a='python 1111 java678php'

r = re.findall('[a-z][a-z][a-z]',a)
print(r) # 输出: ['pyt', 'hon', 'jav', 'php']

r = re.findall('[a-z]{3}',a)
print(r) # 输出: ['pyt', 'hon', 'jav', 'php']


"""
10-6 贪婪与非贪婪

[a-z]{3,6}  #贪婪
[a-z]{3,6}? #非贪婪 
"""

## 默认是贪婪模式
r = re.findall('[a-z]{3,6}',a)
print(r) # 输出: ['python', 'java', 'php']

## 设置非贪婪加? ,取最小值为主
r = re.findall('[a-z]{3,6}?',a)
print(r) # 输出: ['pyt', 'hon', 'jav', 'php']