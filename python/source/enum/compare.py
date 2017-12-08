'''
11-4 枚举的比较运算

枚举只能跟枚举比较 ,不可以跟数字 或 大于小于来比较

在同一下枚举下比较才行,不同的枚举比较是错误
'''

from enum import Enum

class VIP(Enum):
    YELLOW =1
    GREEN =2
    BLACK=3
    RED=4

class VIP2(Enum):
    YELLOW =1
    GREEN =2
    BLACK=3
    RED=4    

#1.可以进行等值比较,即自己跟自己, 否则会报错
r = VIP.GREEN == VIP.GREEN     # 输出 True
r = VIP.GREEN == VIP.BLACK     # 输出 False

#2.身份比较is
r = VIP.GREEN is VIP.GREEN     # 输出 True
r = VIP.GREEN is VIP.BLACK     # 输出 False

#不可两个不同类的枚举比较
r = VIP.GREEN is VIP2.GREEN    # 输出 False  

#3.不可以使用大小写
#r=VIP.GREEN > VIP.BLACK        #报错

#4.不可以数字比较
r= VIP.GREEN == 2               # 输出 False


