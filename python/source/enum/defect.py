'''
没有使用枚举的缺陷:  
1.可变
2.没有防止相同标签的功能 (即变量名不能出现相同的)
3枚举值不可更改
'''
from enum import Enum

#1.可变
a = {'yellow':1,'green':2}
a['yellow'] =3
print(a)  # 输出 {'yellow': 3, 'green': 2}

#2.没有防止相同标签的功能 (即变量名出现相同的)

class TypeDiamond():
	yellow =1
	yellow =2

#枚举值不可更改

class VIP(Enum):
    YELLOW =1
    GREEN =2
    BLACK =3
    RED =4

#VIP.YELLOW =6     #报错