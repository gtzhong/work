'''
旅行者
x,y

x=0

3 result =3 
5 result = 8
6 result = 14   

总结是数数是累加的作用

累计计算走了多少步
	使用非闭包方式
	使用闭包方式
'''

#使用非闭包方式

origin =0

def go(step):
    global origin
    new_pos =origin + step
    origin = new_pos
    return new_pos

"""
print(go(2)) # 输出 2
print(go(3)) # 输出 5
print(go(6)) # 输出 11
"""

#使用闭包方式

origin =0

def factory(pos):
    def go(step):
        nonlocal pos    #要设置,否则会报错,因为不是本函数里的  local variable 'pos' referenced before assignment
        new_pos = pos+step
        pos = new_pos
        return new_pos
    return go

tourist = factory(origin)
print(tourist(2)) # 输出 2
print('cell_contents1:'+str(tourist.__closure__[0].cell_contents)) # 输出 2

print(tourist(3)) # 输出 5
print('cell_contents2:'+str(tourist.__closure__[0].cell_contents)) # 输出 5

print(tourist(6)) # 输出 11
print('cell_contents3:'+str(tourist.__closure__[0].cell_contents)) # 输出 11
