
# 字典来代替switch

day = 0

switcher = {
    0:'Sunday',
    1:'Monday',
    2:'Tuesday'
}

# 调用方法一,缺点没有容错性
day_name = switcher[day]
print(day_name)

# 调用方法2
day = 4
day_name = switcher.get(day,'unknow')
print(day_name)



#方法三  每个键值充当函数使用

day=2

def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_defaulty():
    return 'Unkown'


switcher = {
    0:get_sunday,
    1:get_monday,
    2:get_tuesday
}

day_name = switcher.get(day,get_defaulty)()

print(day_name)


