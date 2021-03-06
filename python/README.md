# python
>版本是 Python3  
>学习 http://www.runoob.com/python3  

## 基础
- 基本类型 @七月
	- [整型与浮点型](fn/base.md#整型与浮点型) 
	- [10,2,8,16进制及转换](fn/base.md#10,2,8,16进制及转换) 
	- [布尔与复数](fn/base.md#布尔与复数) 
	- 字符串
		- [单引号与双引号](fn/base.md#单引号与双引号) 
		- [多行字符串](fn/base.md#多行字符串) 
		- [转义字符](fn/base.md#转义字符) 
		- [原始字符串](fn/base.md#原始字符串) 
		- [字符串运算](fn/base.md#字符串运算) 
	- 组概念与定义
		- [列表](fn/base.md#列表) []表示  看作数组
		- [元组](fn/base.md#元组) ()表示
		- [序列总结](fn/base.md#序列总结)
		- [set集合](fn/base.md#set集合) 无序 {}表示
		- [dict字典](fn/base.md#dict字典) key/value {key1:value1,key2:value2...}
	- 变量与运算符
		- [值类型与引用类型](fn/base.md#值类型与引用类型)
		- [可变与不可变](fn/base.md#可变与不可变)
		- [赋值运算符](fn/base.md#赋值运算符)
		- [关系运算符](fn/base.md#关系运算符)
		- [逻辑运算符](fn/base.md#逻辑运算符)
		- [成员运算符](fn/base.md#成员运算符)
		- [身份运算符](fn/base.md#身份运算符)
		- [如何判断变量的值_身份与类型](fn/base.md#如何判断变量的值_身份与类型)
		- [位运算符](fn/base.md#位运算符)
- 条件控制
	- [if/elif](fn/base.md#if/elif) 
	- [try/except/while](fn/base.md#try/except/while)  
- while循环
	- [while_计算总和](fn/base.md#while_计算总和) 
	- [rang计算总和](fn/base.md#rang计算总和) 
	- [无限循环](fn/base.md#无限循环) 
	- [while循环使用else语句](fn/base.md#while循环使用else语句) 
- for
	- [循环输出数组](fn/base.md#循环输出数组)
	- [多次循环输出数组](fn/base.md#多次循环输出数组)
	- [循环使用break](fn/base.md#循环使用break)
- break和continue
	- [break和continue语句及循环中的else子句](fn/base.md#break和continue语句及循环中的else子句)
	- [continue语句](fn/base.md#continue语句)
- 函数
	- range  遍历数字序列
		- [生成数列](fn/base.md#生成数列) range(5)
		- [指定区间的值](fn/base.md#指定区间的值) range(5,9)
		- [步长](fn/base.md#步长) range(0, 10, 3)
		- [结合range()和len()函数以遍历一个序列的索引](fn/base.md#结合range()和len()函数以遍历一个序列的索引)
	- enumerate 
		- [for i,j](fn/base.md#for i,j)
	- [input](source/input.py)
	- python不建议使用switch 
		- 举例
		- [字典来代替switch](source/dict2switch.py)
	- 函数没有使用return 会返回None
	- [返回多个结果](fn/base.md#返回多个结果)
		- [输出方式1](fn/base.md#输出方式1)
		- [输出方式2](fn/base.md#输出方式2)
	- [序列解包](source/series.py)
	- [默认参数](source/def_student.py)
		- 传实参变量名,可改变顺序
	- 可变参数
		- [1个星号](source/variableParam/simple.py)
			- [1个星号多参数](source/variableParam/simple2.py)
			- [计算平方](source/variableParam/square.py)
		- [2个星字](source/variableParam/temperature.py)
			- [2个星字多参数](source/variableParam/temperature2.py)
	- 变量作用域
		- [内部变量](source/variable/t1.py)
		- [使用域链](source/variable/t3.py)
		- [global](source/variable/global.py)
	- 列表推导式
		- 支持
			- 集合推导式
			- map
			- set 也可以被推导 
			- dict 也可以被推导 
			- 元组
		- 举例
			- [对数组里的数字进行平方](source/tui/square.py#对数组里的数字进行平方)
			- [什么时候使用_列表推导式_有条件筛选](source/tui/square.py#什么时候使用_列表推导式_有条件筛选)
			- [set也可以被推导](source/tui/square.py#set也可以被推导)
			- [dict也可以被推导](source/tui/square.py#dict也可以被推导)
			- [获取字典的key](source/tui/square.py#获取字典的key)
			- [字典的key和value颠倒](source/tui/square.py#字典的key和value颠倒)
			- [打印出元组](source/tui/square.py#打印出元组)
	- None表空
		- [举例](source/tui/none.py)
			- if not a  是否相等 if a is not 
			- 简单的使用 if a:/if not a:
- 包
	- import
		- [import t.t1](source/seven/import_a.py)
		- [import t.t1 as m](source/seven/import_b.py)
	- from
		- [from t.t1 import](source/seven/from_a.py)
		- [from t import t1](source/seven/from_b.py)
		- [from t.t1 import *](source/seven/from_c.py)  导入无限入
		- [from show import (a,b,c)](source/seven/from_d.py)导入多个
	- [过滤变量的外部调用](source/seven/t/t1.py)  __all__
		- [模块文件过滤变量输出](fn/base.md#模块文件过滤变量输出)
		- [过滤模块文件的导入使用](fn/base.md#过滤模块文件的导入使用)
	- 内置变量
		- [import调用内置变量](fn/base.md#import调用内置变量)
		- [入口文件与导入文件的内置变量的区别](fn/base.md#入口文件与导入文件的内置变量的区别)
		- [判断该文件是否入口文件](fn/base.md#判断该文件是否入口文件)
		- 强制模块运行  python -m seven.c15
	- 相对与绝对
		- 入口文件没有顶级包概念
		- 绝对路径引入 
			- import package2.package4.m2 
		- 相对路径引入 
			- from .package2.package4.m2 import m
			-  . .. ...  (1个点表当前目录,2个点上级  3个点以此类推)
- 迭代器 iter 和 next 
	- [逐条输出](fn/base.md#逐条输出)
	- [for遍历](fn/base.md#for遍历)
	- [使用sys模块,使用next()](fn/base.md#使用sys模块,使用next())
- 生成器
	-  [yield实现斐波那契数列](fn/base.md#yield实现斐波那契数列)
- 匿名函数
	- lambda parameter_list:expression(表达式,不做复杂的业务逻辑)
	- [与函数比较](source/lambda.py)
- 三元表达式
	- x>y ? x:y
	- r = x if x> y else y
		- 条件为真时返回的结果 if条件判断 else 条件为假时的返回结果
	- [举例](source/termary.py)
- 高阶函数
	- map
		- [对数据的每个值进行平方举例](source/map/square.py)
		- [map与lambda](source/map/square.py#map与lambda)
			- 上述传入两个参数
			- 并不会报错,就是少输出对应的值
				- list_y少了几个值
				- list_x少了几个值
	- reduce
		- 跟map相比,lambda传入两个参数,后面不用带对应的两个参数,仅一个就够
		- 连接计算,连续调用lambda
		- 大数据
			- map/reduce 编程模型 映射 归约 并行计算
		- reduce第三个参数,初始值 
			- [举例](source/reduce.py)
				- 对数组的累加
	- filter
		- filter返回的为True即可过滤
		- [举例](source/filter.py)
			- 将数据里的0去掉
- 装饰器 @七月
	- 特性 注解 
	- @的精髓使用,使用原来的函数名调用即可
	- 装饰器体现AOP思想
	- 举例
		- 如果有100个函数,都要输出时间那怎样处理呢?
			- [方案A 最笨的方式](source/decorate/a.py)
			- [方案B 对功能封装,调用输出](source/decorate/b.py)
			- [方案C @的精髓使用,使用原来的函数名调用即可](source/decorate/c.py)
			- [方案D 带一个参数的装饰器](source/decorate/d.py)
			- [方案F 带多个参数的装饰器](source/decorate/e.py)
			- [最终方案 带多个参数的装饰器优化](source/decorate/f.py)
				通杀变态的参数长度 func(*args,**kw)
		- [flask_demo](source/decorate/flask.py)
- 变量作用域
	- global和nonlocal关键字 #当内部作用域想修改外部作用域的变量时
		- [global_demo](fn/base.md#global_demo)
		- [nonlocal_demo](fn/base.md#nonlocal_demo)
- 类对象
	- 类的专有方法
		- `__init__` : 构造函数，在生成对象时调用
		- `__del__` : 析构函数，释放对象时使用
		- `__repr__` : 打印，转换
		- `__setitem__` : 按照索引赋值
		- `__getitem__`: 按照索引获取值
		- `__len__`: 获得长度
		- `_cmp__`: 比较运算
		- `__call__`: 函数调用
		- `__add__`: 加运算
		- `__sub__`: 减运算
		- `__mul__`: 乘运算
		- `__div__`: 除运算
		- `__mod__`: 求余运算
		- `__pow__`: 称方
	- 私有变量前面加__ 	如	__secretCount = 0
	- 私有方法前面加__	如  def __foo(self): 
	- [访问类的属性和方法](fn/base.md#访问类的属性和方法)
	- [构造函数__init__](fn/base.md#构造函数__init__)
	- [self代表类的实例_而非类](fn/base.md#self代表类的实例_而非类)
	- [类的方法_def和self](fn/base.md#类的方法_def和self)
	- [继承](fn/base.md#继承)
	- [多继承](fn/base.md#多继承)
	- [方法重写](fn/base.md#方法重写)
	- [运算符重载](fn/base.md#运算符重载)
	- @七月
		- [简单的student类](source/class/student.py)
		- [实例调用student类](source/class/show.py)
		- [__dict__应用](source/class/dict.py)
		- 实例方法
			- [内部外部访问类变量](source/class/visitClass.py)
		- 类方法
			- [每实例一个类,班类总数+1](source/class/funClass.py)
		- 静态方法
			- [静态方法与类方法比较](source/class/staticClass.py)
		- 成员可见性
			- [真假私有变量比较](source/class/privateClass.py)
		- 调用
			- [继承父类构造方法](source/class/overClass.py)
		- 成员可见性
			- 默认公开
			- 没有什么是不能访问
			- 私有方法及变量
				- 定义名字前加 __
			- 举例
				- 真假私有变量比较
		- 三大特殊
			- 继承性
				- 单继承
				- 多继承
			- 封装性
			- 多态性
		- __len__与__bool__内置方法
			- __len__
				- 举例
					- [默认返回true](source/class/len_bool.py#默认返回true)
					- [如果__len__,return 0 则为False,否则为True](source/class/len_bool.py#如果__len__,return 0 则为False,否则为True)
			- __bool__
				- 举例
					- [len()也可以打印 类里的__len__()方法](source/class/len_bool.py)
					- [则优先取__bool__ ,否则就取__len__](source/class/len_bool.py)
			- __nonzero__ python2的 ,被 __bool__替代啦
- 正则 @七月
	- 函数
		- [简单查询index及in](source/regular/index_in.py)
		- re.findall
			- [re.findall常用](source/regular/findall.py)
			- [数量词及贪婪与非贪婪](source/regular/isGreed.py)
			- [匹配0次1次或者无限多次](source/regular/01.py)
			- [边界匹配符使用](source/regular/border.py)
			- 组
				- [组_group应用](source/regular/group.py)
				- [匹配两个单词在字符串](source/regular/group2.py) r.group()  r.groups()
			- 第三个参数 匹配模式参数
				- re.I	忽略大小写	
				- re.S  表匹配除换行符\n之外其它所有字符 
					- [忽略大小写及除换行符的所有字符](source/regular/pattern.py)
		- re.sub
			- [re.sub正则替换](source/regular/sub01.py)
			- [re.sub把函数作为参数传递](source/regular/sub02.py)
		- [search与match函数](source/regular/match_search.py)
- 枚举 @七月
	- 要使类成为枚举的话,必须继承Enum
		- [定义黄钻绿岾黑钻红钻](source/enum/define.py)
	- 枚举和普通类相比有什么优势
		- 没有使用枚举的缺陷
			- 可变
			- 没有防止相同标签的功能
		- 枚举值不可更改
		- [举例](source/enum/defect.py)
	- 区分
		- 枚举名字
		- 枚举的值
		- 枚举类型
		- [举例](source/enum/diff.py)
			- 区分名字/值/类型
			- 遍历枚举
	- 枚举的比较运算
		- 可以进行等值比较
		- 身份比较is
			- 不可两个不同类的枚举比较
		- 不可以数字比较
		- 不可以使用大小写
		- [举例](source/enum/compare.py)
	- 枚举注意事项
		- 枚举里相同的标签(变量名)不可以一样
		- 不同的标签里,可以出现相同的值如
		- [举例](source/enum/attention.py)
			- 不同的标签里,可以出现相同的值如
			- 遍历的情况下,如果数值出现相同
			- 打印别名出来
				- __members__
				- __members__.items()
	- 枚举转换
		- 建议
			- 枚举存数据库,建议保存数字
		- 数字转换为枚举类型
		- [举例](source/enum/convert.py)
	- 怎样限定不能出现相同的值?
		- [举例](source/enum/enum_intEnum.py)
	- 怎样限定不能出现相同的值?
		- [举例](source/enum/filterSameValue.py)
-闭包 @七月
	- 描述
		- 闭包 = 函数+环境变量 (函数定义时候)
		- 现场
		- 函数的外部间接访问函数内部的变量
		- 闭包的好处,保存着上一次的值
	- 举例
		- [最简单的例子](source/closure/simple.py)
			- 环境变量,不受外部的影响
			- 获取闭包的对象
				- __closure__
			- 获取内部的变量
				- __closure__[0].cell_contents
		- [不算是闭包,因为a受外面的影响了](source/closure/no_closure.py)
		- [闭包执行顺序](source/closure/order.py)
		- 闭包的经典误区
			- [判断是否团包](source/closure/is_closure.py)
				- print(f.__closure__)  #报错为 NoneType
				- 无论有没有设置return
		- [累计计算走了多少步](source/closure/walk.py)
			- 使用非闭包方式
			- 使用闭包方式
- 案例
	- 爬虫
		- 熊猫tv分类
			- [举例](source/panda/spider.py)
		- 爬虫套路
			- 定义标签选取
				- 定义标签  唯一性  找最近
				- 举例
					- [字节码转换为字符串](fn/base.md#字节码转换为字符串)
			- 选取闭合的
				- 关系定位标签 父与子关系
			- 使用组过滤头与尾
				- [\s\S]*?
				- 举例
					- [怎样去掉匹配的头与尾的标签](fn/base.md#怎样去掉匹配的头与尾的标签)
			- 循环抓取列表的值
	- [日志ip统计及地址位置限制输出](source/count_log_ip/count.py)
- Python3标准库
	- [操作系统接口](fn/base.md#操作系统接口)
		- os.getcwd()
		- 进入目录 os.chdir('/server/accesslogs')
		- 创建目录  os.system('mkdir today')
- fn
	- python自动化运维篇
		- [ansible](fn/auto_op.md#ansible) [自动化管理IT资源工具]
			- [ansible安装](fn/auto_op.md#ansible安装)
			- [Ansible配置文件路径](fn/auto_op.md#Ansible配置文件路径)
			- [Ansible配置文件获取](fn/auto_op.md#Ansible配置文件获取)
			- 实战操作 (至少须要有2个服务器)
				- [ansible新手上路](fn/auto_op.md#ansible新手上路)
		- [saltstack](fn/auto_op.md#saltstack)
			- [saltstack安装](fn/auto_op.md#saltstack安装)
			- [SaltStack启动](fn/auto_op.md#SaltStack启动)
			- [SaltStack测试](fn/auto_op.md#SaltStack测试)
		- [nagios](fn/auto_op.md#nagios)
			- [nagios安装](fn/auto_op.md#nagios安装)
			- [nagios配置文件](fn/auto_op.md#nagios配置文件)
			- [Nagios主配置文件](fn/auto_op.md#Nagios主配置文件)
			- [nagios安装使用](fn/auto_op.md#nagios安装使用)

