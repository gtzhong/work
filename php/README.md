# PHp

- 干货
	- [符合PSR-1/PSR-2的PHP编程规范实例](standard.php)
- 类库 工具库
	- [db](fn/lib/db.php) @WiconWang
	- 
- function
	- 函数
		- array_walk
			- [购物车实例](fn/Closure.md#购物车实例)  array_walk
			- [把数组(可多维)中值null转为空](fn/op.md#把数组(可多维)中值null转为空) 		
			- [二维数组自定义键str转numberic](fn/op.md#二维数组自定义键str转numberic) 	
			- [等同于foreach](fn/op.md#等同于foreach)
			- [多个array_walk使用](fn/op.md#多个array_walk使用)
			- [路由自定义组装](fn/op.md#路由自定义组装)
			- [tp_清除缓存](fn/op.md#tp_清除缓存) [大雄]
		- strncmp
			- [IP星号匹配](fn/op.md#IP星号匹配) 如192.168.2.1 是不是192.168.*
		- array_map 
			- [调用自定义函数](fn/op.md#调用自定义函数)
			- [内置函数strtoupper](fn/op.md#内置函数strtoupper)
		- fnmatch
			- [正则匹配文件名](fn/op.md#正则匹配文件名)
			- [yii匹配例子](fn/op.md#yii匹配例子)
		- call_user_func
			- [调用一般的函数](fn/op.md#调用一般的函数)
			- [调用对象的方法](fn/op.md#调用对象的方法)
			- [调用对象的静态方法](fn/op.md#调用对象的静态方法)
		- 四舍五入与非
			- printf('%.2f',8.576);  //8.58
			- number_format(8.576,2);	//8.58
			- bcdiv(8.576,1,2);	//8.57
		- 可变参数列表
			- [实现方式1](fn/op.md#实现方式1)  5.5及更早
				- func_get_args
				- func_get_arg
				- func_num_args 等同于 count
			- [实现方式2](fn/op.md#实现方式2)
    - 功能模块
	    - [二维数组自定义键str转numberic](fn/op.md#二维数组自定义键str转numberic) 	
	    - [把数组(可多维)中值null转为空](fn/op.md#把数组(可多维)中值null转为空) 	
	    - [获取当前时间戳_精确到毫秒](fn/fn_module.md#获取当前时间戳_精确到毫秒) 
	    - [需要反序列化的-反序列化](fn/fn_module.md#需要反序列化的-反序列化) 
	    - [时间戳相差输出](fn/fn_module.md#时间戳相差输出) 
	    - [打印输出_pt](fn/fn_module.md#打印输出_pt)  @tianle
	    - [打印输出_dp](fn/fn_module.md#打印输出_dp)  @tianle [常用]
	    - [字符串截取_单字节截取模式](fn/fn_module.md#字符串截取_单字节截取模式) 
	    - [用于生成随机的数字和字母组合](fn/fn_module.md#用于生成随机的数字和字母组合) 
	    - [随机数字数字](fn/fn_module.md#随机数字数字) 
	    - [验证手机号码](fn/fn_module.md#验证手机号码) 
	    - [导出excel封装方法](fn/fn_module.md#导出excel封装方法) 
	    - [身份证号验证](fn/fn_module.md#身份证号验证) 
	    - [出月份的第一天最后一天及当月有多少天](fn/fn_module.md#出月份的第一天最后一天及当月有多少天) 
	- 闭包与匿名函数
		- create_function() [PHP4.1和PHP5中就有了]
			- 不是真正的匿名函数,因为该函数是**有函数名**
			- 只是创建卫一个全局唯一的函数而已
		- Closure	【匿名函数/闭包函数】
			- [__invoke魔幻方法](fn/Closure.md#__invoke魔幻方法) 
			- [匿名函数的实现](fn/Closure.md#匿名函数的实现) 
			- use
				- 在普通函数中当做参数传入也可以被返回
					- [在函数里定义一个匿名函数_并且调用它](fn/Closure.md#在函数里定义一个匿名函数_并且调用它) 
					- [在函数中把匿名函数返回_并且调用它](fn/Closure.md#在函数中把匿名函数返回_并且调用它) 
					- [把匿名函数当做参数传递_并且调用它](fn/Closure.md#把匿名函数当做参数传递_并且调用它) 
					- [直接将匿名函数进行传递](fn/Closure.md#直接将匿名函数进行传递) 
				- 实例 use $name[只复制变量一份],use &$name[绑定上下变量关系]
					- [普通use使用](fn/Closure.md#普通use使用) 
					- [use使用其外部作用域的变量](fn/Closure.md#use使用其外部作用域的变量)
					- [yii2关联查询用use加载外界参数](fn/Closure.md#yii2关联查询用use加载外界参数)
					- [购物车实例](fn/Closure.md#购物车实例)  [array_walk]
				- [闭包函数_参数类型为Closure](fn/Closure.md#闭包函数_参数类型为Closure)
	- 递归
		- [简单的递归例子](fn/recursion/README.md#简单的递归例子)
		- 案例
			- [递归前](fn/recursion/hpdisplayarea-13671.php)
			- [递归后](fn/recursion/HpDisplayArea-13724.php)
			- [我的递归例子](fn/recursion/t7.php)
			- [钱100的递归例子](fn/recursion/钱100.php)
	- 跨域
		- 头部设置
			- 头允许跨域
			```
			// 允许 fizzday.net 发起的跨域请求
			header("Access-Control-Allow-Origin: fizzday.net"); 
			
			//如果需要设置允许所有域名发起的跨域请求，可以使用通配符 *
			header("Access-Control-Allow-Origin: *");
			```
 			- [yii店铺设置_后端跨域解决方案](../yii2/shop.md#1后端跨域解决方案)
 			- [php后端跨越的代码](fn/fn_corss_domain.md#php后端跨越的代码)   [Trait]
		- jsonp跨域
			- jsonp不支付post
			- example
				- [b.com请求a.com](fn/jsonp.md#b.com请求a.com)  
					- 请求与返回都要定义callback对应的名称
		- 设置P3P头,IE有安全策略限制页面不带cookie,针对IE旧版本,firefox与谷歌没有问题
	- 模拟表单提交 @ghost Wu
		- fiddler抓包
		- [file_get_contents或fopen_post](fn/simulation_post.md#file_get_contents或fopen_post)
		- curl
			- [curl_post](fn/simulation_post.md#curl_post)
			- [curl_参数封装_curl_setopt_array](fn/simulation_post.md#curl_参数封装_curl_setopt_array)
		- socket [fsockopen]
			- 访问socket存在慢
				- [socket_post](fn/simulation_post.md#socket_post)
			- 解决socket慢
				- [优化解决socket访问慢](fn/simulation_post.md#优化解决socket访问慢)
				- [socket函数封装_提供post与get选择_支持cookie](fn/simulation_post.md#socket函数封装_提供post与get选择_支持cookie)
		- socket [socket_create]
			- 农行的demo
				- [socket整理](socket.md#socket整理) 
				- [查询](socket/s1.php) 
				- [分账](socket/c1.php)
		- 案例
			- 旅游分销API接口
				- [众信的对接接口](http://agent.utourworld.com/loadApiWeb) 使用报文形式发送
					- [众信系统对接说明](socket/众信系统接口对接流程说明-171025.docx) 
	- rsa
		- [php_rsa](fn/rsa/rsa_php_source/php_rsa.php)
		- [模拟登陆_vding](../yii2/vding_api.md#模拟登陆_vding) //其它系统获取登陆token
	- 高并发处理
		- redis
			- [redis的List类型实现秒杀_例子](fn/redis/miaosha.md#redis的List类型实现秒杀_例子)
				- LPUSH/LPUSHX :将值插入到（/存在的）列表头部
				- RPUSH/RPUSHX :将值插入到（/存在的）列表尾部	
				- LPOP :移出并获取列表的第一个元素
				- RPOP :移出并获取列表的最后一个元素
				- LTRIM :保留指定区间内的元素
				- LLEN  :获取列表长度
				- LSET  :通过索引设置列表元素的值
				- UNDEX :通过索引获取列表中的元素
				- LRANGE :获取列表指定范围内的元素
		- [RabbitMQ](fn/RabbitMQ/README.md)  更专业的消息系统实现方案  @WiconWang
- 面向对象
	- 常用类
		- Closure        闭包类，匿名函数对象的final类
		- stdClass    标准类，通常用于对象类保存集合数据
		- __PHP_Incomplete_Class        不完整类，当只有对象而没有找到类时，则该对象被认为是该类的对象
		- Exception    异常类
		- PDO            数据对象类
	- 魔术常量
		- __DIR__            文件所在的目录
		- __LINE__        文件中的当前行号 
		- __FILE__        文件的完整路径（绝对路径）和文件名
		- __CLASS__        类的名称
		- __METHOD__        类的方法名，包含类名和方法名
		- __FUNCTION__    函数名称，用在方法内只表示方法名
	-  类与对象·关键字
		- this        代表本对象
		- public        公有的（继承链、本类、外部均可访问）
		- protected    保护的（仅继承链、本类可访问）
		- private        私有的（仅本类可访问）
		- parent::    代表父类
		- self::        代表本类(当前代码所在类)
		- static::    代表本类(调用该方法的类)
		- static        静态成员（属性、方法），所有对象均可使用，外部也可直接使用或修改，静态方法不可访问非静态成员
		- final        方法用final不可被子类重载，类用final不可被继承（方法、类）
		- const        类常量（属性）
		- abstract    抽象类
		- interface    接口
		- extends        类继承(子接口继承接口、其他普通类继承)
		- implements    接口实现（类实现接口、抽象类实现借口）（对接口的实现和继承均可有多个）
		- Iterator    内置接口（迭代）
		- clone        克隆
		- instance    实例
		- instanceof    某对象是否属于某类
	-  属性重载
		- 处理不可访问的属性
		属性重载只能在对象中进行。
		-  属性重载对于静态属性无效
		在静态方法中，这些魔术方法将不会被调用。所以这些方法都不能被声明为static。
		- __set   在给不可访问的属性赋值时

		  ``` 
			 public void __set(string $name, mixed $value)
		    作用：批量管理私有属性，间接保护对象结构
		  ```	
		- __get   读取不可访问的属性的值时

			 ``` 
		    public mixed __get(string $name)
			 ``` 
		- __isset  当对不可访问的属性调用isset()或empty()时

			 ``` 
		    public bool __isset(string $name)
			 ``` 
		- __unset   当对不可访问的属性调用unset()时|

			 ``` 
		    public void __unset(string $name)
			 ``` 
	-  方法重载
		- 处理不可访问的方法
		- __call            当调用一个不可访问的非静态方法（如未定义，或者不可见）时自动被调用

		        public mixed __call(string $name, array $arguments)
		- __callStatic    当在调用一个不可访问的静态方法（如未定义，或者不可见）时自动被调用

		        public static mixed __callStatic(string $name, array $arguments)
		-  $name参数是要调用的方法名称。$arguments参数是一个数组，包含着要传递给方法的参数。
	- 常用函数
		- [get_class](object_fn.md#get_class) //获取类名
		- [instanceof](object_fn.md#instanceof) //某个对象是不是属于某个类的继承
		- [get_class_methods](object_fn.md#get_class_methods) //类中所有方法列表
		- 检测方法是否在类中存在
			- [get_class_methods](object_fn.md#get_class_methods) 
			- [method_exists](object_fn.md#method_exists) 
			- [is_callable](object_fn.md#is_callable) 
		- get_class_vars()  //查询类的属性
		- 类的继承关系
			- get_parent_class   //找类的父类
			- is_subclass_of	//检测类是否属于另个一个类的派生类
			- instanceof		//检测类是否实现某个接口
			- [class_implements](object_fn.md#class_implements)  
		- 查找类
			- class_exists		//检查类是否存在
		- autoload 	自动加载
			- [发送微信号或发送短信例子](object_fn.md#发送微信号或发送短信例子)
	-  反射机制 Reflection
		- 作用：1. 获取结构信息        2. 代理执行
		- ReflectionClass 报告一个类的有关信息
		- ReflectionMethod 报告一个方法的有关信息
		- ReflectionClass::export    输出类结构报告
		- [yii2_admin_反射获取action](../yii2/fn/yii2_admin/README.md#yii2_admin_反射获取action)
	- 抽象类 	abstract
		 - [基本的定义与使用](object_class.md#基本的定义与使用)  
	- Traits	//代码复用的一个方法,为了减少单继承语言的限制，使开发人员能够自由地在不同层次结构内独立的类中复用方法集
		 - 删除的公共方法例子
		 - 例子
			 - [php后端跨越的代码](fn/fn_corss_domain.md#php后端跨越的代码)   [Trait] [跨域]
			 - [短信模块_zhou](fn/fn_corss_domain.md#短信模块_zhou)
	- stdClass使用
		- [认证宝stdClass使用](fn/stdClass.md#认证宝stdClass使用)
	- 对象常用总结
		- [静态变量存取_对象自身实例化](fn/objeck_of.md#静态变量存取_对象自身实例化)
- RestfulApi
	- 会飞的鱼Xia
		- [例子说明_会飞的鱼Xia](RestfulApi.md#例子说明_会飞的鱼Xia)
		- [RestfulApi初始化](https://github.com/408824338/RestfulApi_i/blob/master/restful/index.php)
		- [使用postman授权设置与使用](RestfulApi.md#使用postman授权设置与使用)
		- [代码中使用用户与密码来登陆](RestfulApi.md#代码中使用用户与密码来登陆)
		- 本例子中使用php://input来获取参数,我使用postman来模拟,获不取不到数据
		- 什么时候使用file_get_contents('php://input') 
	- [使用postman模拟参数php解析获取](shop.md#使用postman模拟参数php解析获取)   // PHP_AUTH_USER 和  PHP_AUTH_PW
- composer
	- 常用 
		- C:\Users\cmk\AppData\Local\Composer window路径 
		- composer clear-cache 清空缓存
		- composer update fihacklog/yii2-sms-module  单个更新
		- composer update ihacklog/yii2-sms-module  --prefer-source 更换仓库
	- 问题
		- 1.某个包加载使用指定的仓库,修改该仓库地址,一直无法更新
		- 回答:
			- 1.临时方案,进入该目录,执行git pull origin master
			- 2.彻底的解决办法:将composer.lock删除,再执行composer install
			- 3.如果是开发环境,则将ventor删除,如果是线上,则复制文件上去
			- 4.亲测 
				- 4.1 指定版本 "horse003/yii2-event-demo": "^1.0.2",
				- 4.2 指定更新 composer update horse003/yii2-event-demo
	- 上传到composer
		- 代码上传至github
		- https://packagist.org 注册并登陆
		- [composer.json_标准参考文件](fn/composer/README.md#composer.json_标准参考文件)
		- [packageist设置](fn/composer/packageist设置)
		- [使用打标签更新代码](fn/composer/README.md#使用打标签更新代码)
		