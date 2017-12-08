'''
11-6 枚举转换

枚举存数据库,建议保存数字

数字转换为枚举类型
'''

from enum import Enum

class VIP(Enum):
    YELLOW =1
    GREEN =2
    BLACK=3
    RED=4

a = 1
print(VIP(a))   #输出: VIP.YELLOW
print(VIP(a).name)   #输出 : YELLOW
print(VIP(a).value) #输出 : 1