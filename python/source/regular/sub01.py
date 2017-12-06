'''
10-11 re.sub正则替换
re.sub()

#第4个参数,替换的次数,默认0为无限

language.replace()  //re.sub()的简化版

函数代替参数

'''

import re
language = 'PythonC#JavaPHPC#PHPC#'
r = re.sub('C#','GO',language)
print(r)  # 输出: PythonGOJavaPHPGOPHPGO

r = re.sub('C#','GO',language,1)
print(r)  # 输出: PythonGOJavaPHPC#PHPC#


## 函数代替参数

def convert(value):
    #print(value)  # 输出: <_sre.SRE_Match object; span=(6, 8), match='C#'>
    matched = value.group()
    return '!!'+matched+'!!'

r = re.sub('C#',convert,language)
print(r)  # 输出: Python!!C#!!JavaPHP!!C#!!PHP!!C#!!






