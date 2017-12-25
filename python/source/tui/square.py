'''
列表推导式  

i的平方
1. i*i
2. i**2


a= [1,2,3,4,5,6,7,8]
b= [i**2 for i in a]
print(b)

求立方
a= [1,2,3,4,5,6,7,8]
b= [i**3 for i in a]  # 等同于  i*i*i
print(b)


set也可以被推导 
dict也可以被推导 


'''


# 对数组里的数字进行平方
a =[1,2,3,4,5,6,7,8]

## 方式1
b=[i*i for i in a]
print(b)  # 输出 [1, 4, 9, 16, 25, 36, 49, 64]

## 方式2
b=[i**2 for i in a]
print(b)  # 输出 [1, 4, 9, 16, 25, 36, 49, 64]

## 求立方
b=[i**3 for i in a]
print(b)  # 输出 [1, 8, 27, 64, 125, 216, 343, 512]


## 什么时候使用_列表推导式_有条件筛选


a =[1,2,3,4,5,6,7,8]
# 如求大于等于5的.才求平方
b = [i**2 for i in a if i>=5]
print(b)  # 输出  [25, 36, 49, 64]


# set也可以被推导 
a= {1,2,3,4,5,6,7,8}
##如求大于等于5的.才求平方
b= {i**2 for i in a if i>=5}
print(b)  # 输出  {64, 25, 36, 49}



# dict也可以被推导 

'''
字典被for的时候,要输出两个参数
[key for key,value in students.items()]
'''

# 获取字典的key
students = {
	'张三':18,
	'李四':20,
	'王八':15
}

b = [key for key,value in students.items()]
print(b)  # 输出 ['张三', '李四', '王八']

# 字典的key和value颠倒
b={value:key for key,value in students.items()}
print(b)  # 输出 : {18: '张三', 20: '李四', 15: '王八'}

# 打印出元组
b = {value:key for key,value in students.items()}
for x in b:
    print(x)

"""
输出
18
20
15
"""









