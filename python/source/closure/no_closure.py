'''
不算是闭包,因为a受外面的影响了

'''

a=25 
def curve_pre():
    def curve(x):
        return a*x*x
    return curve

a=10
f=curve_pre()
print(f(2))  # 输出 40
print(f.__closure__)  # 输出 None 表示不是闭包