
'''
# 枚举表示 黄钻 绿岾 黑钻 红钻
'''
from enum import Enum
class VIP(Enum):
    YELLOW =1
    GREEN =2
    BLACK =3
    RED =4

print(VIP.YELLOW)  # 输出  VIP.YELLOW ,而不是数字1