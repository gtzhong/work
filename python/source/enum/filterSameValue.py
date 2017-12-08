'''
怎样限定不能出现相同的值?
'''


from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1  # 报错:执行会提示值重复   duplicate values found in <enum 'VIP'>: GREEN -> YELLOW
    BLACK = 3
    RED = 4


