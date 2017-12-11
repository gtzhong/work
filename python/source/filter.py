'''
#举例 将数据里的0去掉

    方法一
    方法二

# filter返回的为True即可过滤 
'''

list_x = [1,0,1,0,0,1]

## 方法一
r = filter(lambda x : True if x==1 else False,list_x)
print(list(r)) # 输出 [1,1,1]


## 方法二

r = filter(lambda x:x,list_x)
print(list(r)) # 输出 [1,1,1]
