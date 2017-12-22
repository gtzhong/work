'''
14-5 None表空
不等于  

空字符串 空的列表 0  False

类型,值 
'''

a = ''
b = False
c=[]

print(a == None) # 输出:False
print(b == None) # 输出:False
print(c == None) # 输出:False

print( a is None) # 输出:False
print(type(None)) # 输出:<class 'NoneType'>



# if not a  是否相等 if a is not 

def fun():
    return None

a = fun()

if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

"""
输出
S
S
"""  

a = []
if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')


"""
输出
S 
F
"""


'''
简单的使用 
if a:
if not a:  
即可

'''

# 简单的使用 if a:/if not a:

a = None
a=''
a=[]
a=False

