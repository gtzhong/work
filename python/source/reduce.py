'''
对数组的累加
'''

from functools import reduce

list_x = [1,2,3,4,5,6,7,8]

r = reduce(lambda x,y:x+y,list_x)
print(r) # 输出 36   计算规则: (((((1+2)+3)+4)+5)+6)+7


# reduce第三个参数,初始值 
list_x = [1,2,3,4,5,6,7,8]
r = reduce(lambda x,y:x+y,list_x,10)
print(r) # 输出:46


list_x = ['1','2','3','4','5','6','7','8']
r = reduce(lambda x,y:x+y,list_x,'aaa')
print(r) # 输出: aaa1234567


