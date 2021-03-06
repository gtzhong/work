- php操作  
	- 扩展与安装
		- [版本信息](fn/php.md#版本信息)
		- 分类
			- Thread safe(TS)  针对 Apache
			- non-thread safe(NTS) 针对nginx
		- [举例](fn/php.md#扩展与安装)
	- 举例
		- [获取数据](fn/php.md#获取数据)
- 操作使用
	- 常用操作
		- show dbs
			- 查看有多少数据库
		- use  db
			- 选择数据库,如果没有会自动创建
		- db 
			- 查看当前在哪个数据库
		- db.dropDatabase()
			- 删除数据库  先use db
		- mongod --version
			- 查看版本
	- curl 
		- 查询
			- 查询有多少条记录
				- db.imooc_collection.count()
			- 过滤与排序
				- db.article.find().skip(3).limit(2).sort({x:1})
					- 1 从小到大  -1 从大到小
			- 查询指定
				- db.sms.find({num:20})
		- 插入
			- 批量插入记录
				- for(i=1;i<50;i++)db.sms.insert({num:i,name:'test'})
			- 单个字段
				- db.article.insert({title:'某新闻标题'})
			- 多个字段
				 - db.article.insert({title:'某新闻标题',author:'李四'})
		- 更新
			- 不可使用
				db.article.update({x:1},{x:999})
			- 使用$set更新 
				- db.article.update({z:100},{$set:{y:99}})
			- 更新不存在的记录,而自动插入数据,使用第三鼐参数
				- db.article.udpate({x:100},{y:999},true)
			- 多条记录更新,使用第四个参数
				- db.article.update({num:25},{$set:{author:"王八"}},false,true)
		- 删除
			- 删除表
				- db.article.drop()
			- 删除记录
				- db.article.remove({num:25})
		- [举例](fn/curl.txt)
- 索引
	- 分类
		- _id索引
		- 单键索引
			- 单键索引是最普通的索引
				- 例如: 一条记录为{x:1,y:2,z:3}
			- 与_id索引不同,单键索引不会自动创建
			- 操作
				- db.imooc_collection.ensureIndex({x:1})
			- [举例](fn/index.md#单键索引)
		- 多键索引
			- 多键索引与单键索引创建形式相同,区别在于字段的值
			- db.sms.insert({x:[1,2,3,4,5]})
		- 复合索引
			- 当我们索引条件不只有一个时,就需要建立复合索引
			- 插入{x:1,y:2,z:3} 按照x和y值的查询  创建索引如下
				- db.collection.ensureIndex({x:1,y:1})  # 使用{x:1,y:1}作为条件进行查询
				- db.imooc_2.find({x:1,y:2})  #进行复合查询
		- 过期索引
            - 描述
                - 1.索引索引:是在一段时间后过期的索引
                - 2.在索引过期后,相应的数据会被删除
                - 3.场景:登陆信息 存储日志
			- db.collection.ensureIndex({time:1},{expireAfterSeconds:10})
			- 存储在过期索引字段的值必须是指定的时间类型
				- 说明:必须是 ISODate或者ISODate数组,不能使用时间戳,否则不能被自动删除
			- [举例](fn/index.md#过期索引)
        - 全文索引
            - 对字符串与字符串数组创建全文可索引的索引
            - 场景: {author:"",title:"",article:""}
            - 操作
                - 创建索引
                    - db.articles.ensureIndex({key:"text"})
                    - db.articles.ensureIndex({key_1:"text",key_2:"text"})
                    - db.articles.ensureIndex({"$**":"text"})
                - 查询
                    - 普通查询
                        - db.articles.find({$text:{$search:"coffee"}})
                        - db.articles.find({$text:{$search:"aa bb cc"}}) #空格表示或关系 
                        - db.articles.find({$text:{$search:"co bb -cc"}}) # 负号表示不包含
                        - db.articles.find({$text:{$search:"\"aa\" bb cc"}}) #使用双引号表示与的关系 ,必须包括aa关键字
                    - 权重查询
                        - $meta操作符: {score:{$meta:"testScore"}}
                        - db.articles.find({$text:{$search:"aa bb -rr"}},{score:{$meta:"textScore"}})
                        - 排序:db.articles.find({$text:{$search:"aa"}},{score:{$meta:"textScore"}}).sort({score:{$meta:"textScore"}})
            - 全文索引的使用限制
                - 1.每镒查询,只能指定一个$text查询
                - 2.$text查询不能出现在$nor查询中
                - 3.查询中如果包含$test,hint不再起作用
                - 4.不支持中文
            - 举例
                - [使用全文索引进行查询](fn/index.md#使用全文索引进行查询)
                - [全文索引相似度(搜索权重)](fn/index.md#全文索引相似度查询)
			- 自定义索引
				- 一个索引字段名只能添加一次
				- 索引属性—name指定
					- 创建索引时的格式
						- db.collection.ensureIndex({param},{name:""}) #其中第二个参数便是索引的属性
						- db.imooc_2.ensureIndex({x=1,y=1},{name:"normal_index") #创建normal_index命名的索引
						- db.imooc_2.dropIndex("normal_index")  #删除索引
				- 索引属性—unique指定
					- 唯一性 格式
						- db.collection.ensureIndex({},{unique:true/false})
						- db.imooc_2.ensureIndex({m:1,n:1},{unique:true})
						- db.test.ensureIndex({num:1},{unique:true})  #1为正序 -1 降序
				- 索引属性—sparse和expireAfterSeconds指定
					- 描述
						- 默认创建索引是不稀疏
						- 稀疏好处 对不存在的数据,不创建索引
					- 稀疏性,spare指定 格式 
						- db.collection.ensureIndex({},{spare:true/false})
				- 举例
					- [name指定](fn/index.md#name指定)
					- [unique指定](fn/index.md#unique指定)
					- [sparse和expireAfterSeconds指定](fn/index.md#sparse和expireAfterSeconds指定)
			- 地理位置索引
				- 概念:将一些点的位置存储到MongoDB中,创建索引后,可以按照位置来查找其他点
				- 子分类
					- 2d索引,用于存储和查找平面上的点
					- 2dsphere索引,用于存储和查找球面上的点
				- 查找方式
					- 1.查找距离某个点一定距离范围内的点 ,如打车或外卖的地理
					- 2.查找包含在某区域内的点
				- 2D索引详解
					- 创建方式
						- db.collection.ensureIndex({w:"2d"})
					- 位置表示方式:经纬度[经度,续度]
					- 取值范围:经度[-180,180] 续度[-90,90],否则会出错
					- 查询方式:
						- 1.$near查询:查询距离某个点最近的点
						- 2.$geoWithin查询:查询某个形状内的点
						- 举例
							- [$near查询](fn/index.md#$near查询)
							- [$geoWithin查询](fn/index.md#$geoWithin查询)
								- db.location.find({w:{$geoWithin:{$box:[[0,0],[3,3]]}}})
								- db.location.find({w:{$geoWithin:{$polygon:[[0,0],[0,1],[2,5],[6,1]]}}})
							-  [使用geoNear查询](fn/index.md#使用geoNear查询)
					- 形状的表示
						- 1.$box:矩形使用
							- {$box:[[<x1>,<y1>,[<x2>,<y2>]]]}
						- 2.$center:圆形使用
							- {$center:[<x1>,<y1>],r}
						- 3.$polygon:多边形使用
							- {$polygon:[[<x1>,<y1>],[<x2>,<y2>],[<x3>,<y3>]]}
				- 2dsphere索引详解
					- 创建方式:
						- db.collection.ensureIndex({w:"2dsphere"})
					- 位置表示方式
						- GeoJSON:描述一个点,一条直线,多边形等形状
					- 格式:
						- {type:" ",coordinates:[<coordinates>]}
					- 查询方式与2d索引查询方式 类似
						- 支持$minDistance与$maxDistance
- 索引构建
	- 4种方式
		- 1.mongostat工具介绍
			- 查看mongodb运行状态的程序
			- mongostat -h 127.0.0.1:12345
			- 字段说明
				- qr  #读队列
				- qw  #写队列
				- 索引情况:idx miss
			- 举例
				- [使用mongostat效果验证](fn/index.md#使用mongostat效果验证)
		- 2.profile集合介绍
			- [举例](fn/index.md#profile集合介绍)
		- 3.日志介绍
			- [举例](fn/index.md#日志介绍)
		- 4.explain分析
			- [举例](fn/index.md#explain分析)
	- MongoDB安全楔子
		- 描述
			- 1.MongoDB安全概览
			- 2.物理隔离与网络隔离
			- 3.IP白名单隔离
			- 4.用户名密码鉴权
		- 开启权限认证
			- 1.auth开启
			- 2.keyfile开启
			- [举例](fn/index.md#开启权限认证)
		- 角色
			- 数据库角色
				- read
				- readWrite
				- dbAdmin
				- dbOwner
				- userAdmin
			- 集群角色
				- clusterAdmin
				- clusterManager
			- 备份角色
				- backup
				- restore
			- 其它特殊权限
				- DBAdminAnyDatabase
		- 创建用户
			- 2.6.5
				- createUser (2.6之前为addUser)
				- db.createUser({user:"admin",pwd:"admin",roles:[{role:"userAdmin",db:"admin"},{role:"read",db:"test"}]})
				- [配置mongod.conf](fn/index.md#2.6.5配置mongod.conf)
			- 3.2.4
				- 首次创建一个用户(该用户仅创建,其它做不了)
					- use admin 
						- db.createUser({user: "super",pwd: "123456",roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]})
				- 创建真正的用户
					- db.createUser({user:" vding",pwd:"123456",roles:[{role:"readWrite",db:"vding"},{role:"read",db:"test"}]})
				- 登陆
					- 方法1
						- mongo -u 帐号名 -p 密码 --authenticationDatabase 数据库名
					- 方法2
						- mongo
						- use  数据库名
						- db.auth("vding","12345678") #认证，返回1表示成功
									- [配置mongod.conf](fn/index.md#3.2.4配置mongod.conf)
		- 删除用户
			- 格式 
				- use test;
					- db.dropUser("admin")
					- db.runCommand( { dropUser: "admin" } )
- 搭建与使用
    - 安装
        - 2.6.5
            - 压缩包安装
            - [举例](fn/install.md#2.6.5压缩包安装)
        - 3.2.4
            - yum安装
                - [官网安装流程](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
            - [举例](fn/install.md#3.2.4yum安装)