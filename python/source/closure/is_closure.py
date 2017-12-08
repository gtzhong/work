'''
闭包的经典误区
	判断是否团包
		print(f.__closure__)  #报错为 NoneType
		无论有没有设置return
'''


# 例A 
def curve_pre():
    a=25
    def curve(x):
        return a*x*x
    return curve

a=10
f=curve_pre()
print(f(2))  # 输出 40
print(f.__closure__) #输出  (<cell at 0x035126B0: int object at 0x627BD8B0>,)  是闭包

# 例B 
def curve_pre2():
    a=25
    def curve(x):
        a=10
        return a*x*x
    return curve

a=10
f=curve_pre2()
print(f(2))  # 输出 40
print(f.__closure__)  # 输出 None 表不是闭包


# 例C
a=25
def curve_pre3():
    def curve(x):
        return a*x*x
    return curve

a=10
f=curve_pre3()
print(f(2))  # 输出 40
print(f.__closure__)  # 输出 None 表不是闭包


# 例C2
a=25
def curve_pre3():
    def curve(x):
        return a*x*x  # 有没有return都一样
    return curve

a=10
f=curve_pre3()
print(f(2))  # 输出 40
print(f.__closure__)  # 输出 None 表不是闭包