'''

10-12 把函数作为参数传递

举例:对字符串里的数字,大于6的变成9 小于6的变成0

'''

import re

s = '8C3721D86'

def convert(value):
    matched = value.group()
    # print(matched)
    # pass
    if int(matched) >=6:
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,s)
print(r)  # 输出 : 9C0900D99