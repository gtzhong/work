
def demo(*param):
    print(param) #传实参变量名,可改变顺序
    print(type(param)) #<class 'tuple'>

#调用方法1
demo(1,2,3,4,5)


#调用方法2
a = (1,2,3,4,5)
demo(*a)