
#遍历字典,获取各城市的温度,因为是二级数据,则使用双号**
def city_temp(**param):
    #print(param)       #输出 {'bj': '32c', 'xm': '23c', 'sh': '31c'}
    #print(type(param)) #输出<class 'dict'>
    for c in param:
        print(c)       
    pass

    """
    输出:
        bj
        xm
        sh
    """

    for key,value in param.items():
        print(key,':',value)
    
    """
     输出:
        bj : 32c
        xm : 23c
        sh : 31c
    """

city_temp(bj='32c',xm='23c',sh='31c')

