'''
最简单的例子
	环境变量,不受外部的影响
	获取闭包的对象
		__closure__
	获取内部的变量
		__closure__[0].cell_contents
'''


def curve_pre():
    a=25     # 环境变量,不受外部的影响
    def curve(x):
        return a*x*x
    return curve

a=10
f=curve_pre()
print(f(2))  # 输出 100

print(f.__closure__) # 输出 (<cell at 0x032326F0: int object at 0x627BD8B0>,)
print(f.__closure__[0].cell_contents)  # 输出 25  获取内部的变量