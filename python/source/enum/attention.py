'''
11-5 枚举注意事项

枚举里相同的标签(变量名)不可以一样
不同的标签里,可以出现相同的值如

'''


from enum import Enum


#不同的标签里,可以出现相同的值如
class VIP(Enum):
    YELLOW =1
    GREEN =1  #这个充当一个别名  可以将名字修改为 YELLOW_ALIAS  = 1
    BLACK=3
    RED=4

print(VIP.GREEN)    #输出:VIP.YELLOW


class VIP2(Enum):
    YELLOW =1
    YELLOW_ALIAS =1  #这个充当一个别名  可以将名字修改为 YELLOW_ALIAS  = 1
    BLACK=3
    RED=4

print(VIP2.YELLOW_ALIAS)    #输出:VIP2.YELLOW

#遍历的情况下,如果数值出现相同

for v in VIP:
    print(v)

"""
输出:
VIP.YELLOW
VIP.BLACK
VIP.RED
"""

for v in VIP.__members__.items():
    print(v)

"""
输出:
('YELLOW', <VIP.YELLOW: 1>)
('GREEN', <VIP.YELLOW: 1>)
('BLACK', <VIP.BLACK: 3>)
('RED', <VIP.RED: 4>)
"""    

for v in VIP.__members__:
    print(v)

"""
输出:
YELLOW
GREEN
BLACK
RED
"""
