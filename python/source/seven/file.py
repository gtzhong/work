#方法1 在本文件里定义

'''
import sys
import datetime
import io

print(sys.path)
'''

# 方法2 在全局__init__定义
## 包和模块是不会被重复导入
## 避免循环导入
import t
print(t.sys.path)
