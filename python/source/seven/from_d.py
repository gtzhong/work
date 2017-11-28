from t.t1 import *
#from t.t1 import (a,b,c) #在这个情况下,虽然上面__all__ = ['a','c'],会失效
print(a)
print(b) # 输出不出来,因为上面过滤
print(c)