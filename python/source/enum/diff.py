'''
区分 枚举类型 枚举名字 枚举的值

遍历枚举
'''

from enum import Enum

class VIP(Enum):
    YELLOW =1
    GREEN =2
    BLACK=3
    RED=4

## 输出类型
print(VIP.GREEN) #输出 VIP.GREEN
print(VIP['GREEN']) #输出 VIP.GREEN

## 输出值
print(VIP.GREEN.value) #输出  2

## 输出名称
print(VIP.GREEN.name) #输出  GREEN


# 遍历枚举
for v in VIP:
    print(v,v.name,v.value)

'''
输出:
VIP.YELLOW YELLOW 1
VIP.GREEN GREEN 2
VIP.BLACK BLACK 3
VIP.RED RED 4
'''