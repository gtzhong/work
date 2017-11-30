#遍历字典,获取各城市的温度,因为是二级数据,则使用双号**
#由于是字典类型,包了一个(键值关系  ),则多加一个*,普通使用一个即可
def city_temp(param1,**param):
    print(param1)   #输出 1
    print(param)    #输出 {}
    for key,value in param.items():
        print(key,':',value)
    

a={'bj':'32c','xm':'23c','sh':'31c'}
city_temp(1)

