'''
[abc] #表 或a 或b 或c
(abc) #表示与  必须同时有abc

(python){3}

'''

import re
a ='PythonPythonPythonPythonPython'

r = re.findall('PythonPythonPython',a)
print(r)    # 输出: ['PythonPythonPython']


r = re.findall('(Python){3}(JS)',a)
print(r)    # 输出: []



