'''
14-7 __len__与__bool__内置方法


'''

# 默认返回true
class Testt():
    pass

print(bool(Testt())) #输出 True


# 如果__len__,return 0 则为False,否则为True  
## 如果输出为字符串则报错
## 如果输出为布尔值为正常

class Testt():
    pass

    def __len__(self):
        return 0

print(bool(Testt())) #输出 False


class Testt2():
    pass

    def __len__(self):
        return 8

print(bool(Testt2())) #输出 True


# len()也可以打印 类里的__len__()方法


class Testbool():
    def __bool__(self):
        return False  # 不可以return 0
    
    def __len__(self):
        return True

print(bool(Testbool()))


class Test3():
    def __bool__(self):
    	print('bool called')
    	return False  # 不可以return 0

    def __len__(self):
        print('len called')
        return True

"""
#输出
bool called
False
"""

print(bool(Test3())) 

class Test4():
    def __len__(self):
        print('len called')
        return True

print(bool(Test4())) 
"""
#输出
len called
True
"""