# 索引

## 单键索引

```
4-3 [mongoDB] 单键索引 (0140)

1.单键索引是最普通的索引
  例如: 一条记录为{x:1,y:2,z:3}

2.与_id索引不同,单键索引不会自动创建


> show tables;
sms
> db.sms.find()
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf57c"), "num" : 1, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf57d"), "num" : 2, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf57e"), "num" : 3, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf57f"), "num" : 4, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf580"), "num" : 5, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf581"), "num" : 6, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf582"), "num" : 7, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf583"), "num" : 8, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf584"), "num" : 9, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf585"), "num" : 10, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf586"), "num" : 11, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf587"), "num" : 12, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf588"), "num" : 13, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf589"), "num" : 14, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf58a"), "num" : 15, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf58b"), "num" : 16, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf58c"), "num" : 17, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf58d"), "num" : 18, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf58e"), "num" : 19, "name" : "test" }
{ "_id" : ObjectId("5a30e53726ca81c5e2bdf58f"), "num" : 20, "name" : "test" }
Type "it" for more

>db.sms.ensureIndex({num:1})   #添加索引  x=1 为正向排序  x=-1 为逆向排序

>db.sms.getIndexes() 

#输出

> db.sms.getIndexes()
[
	{
		"v" : 2,
		"key" : {
			"_id" : 1
		},
		"name" : "_id_",
		"ns" : "vding.sms"
	},
	{
		"v" : 2,
		"key" : {
			"num" : 1
		},
		"name" : "num_1",
		"ns" : "vding.sms"
	}
]
db.sms.find({num:1}) #会使用到索引
```


## 过期索引
-  1.存储在过期索引字段的值必须是指定的时间类型
说明:必须是 ISODate或者ISODate数组,不能使用时间戳,否则不能被自动删除

- 2.如果指定的ISODate数组,则按照最小的时间进行删除

- 3.过期索引不能是复合索引

- 4.删除时间不是精确
  说明:删除过程是由后台程序每60s跑一次,而且删除也需要一些时间,所以存在误差

```mongodb
# 设置一个过期索引为20秒
> db.cookie.ensureIndex({time:1},{expireAfterSeconds:20})
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}

> db.cookie.getIndexes()
[
	{
		"v" : 2,
		"key" : {
			"_id" : 1
		},
		"name" : "_id_",
		"ns" : "vding.cookie"
	},
	{
		"v" : 2,
		"key" : {
			"time" : 1
		},
		"name" : "time_1",
		"ns" : "vding.cookie",
		"expireAfterSeconds" : 20
	}
]


# 分别插入两个信息 
>db.cookie.insert({time:25})  #这个是不会删除
> db.cookie.insert({time:new Date()})

```


# 全文索引

## 使用全文索引进行查询

```mongodb

#插入3个数据
db.articles.insert({"content":"aa bb cc dd ee"})
db.articles.insert({"content":"aa bb rr dd"})
db.articles.insert({"content":"aa bb cc hh dojiofjqjfq"})

#建立全文索引
> db.articles.ensureIndex({content:"text"})
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}

#查询
db.articles.find({$text:{$search:"coffee"}})
db.articles.find({$text:{$search:"aa bb cc"}}) #空格表示或关系 
db.articles.find({$text:{$search:"co bb -cc"}}) # 负号表示不包含
db.articles.find({$text:{$search:"\"aa\" bb cc"}}) #使用双引号表示与的关系 ,必须包括aa关键字

```

## 全文索引相似度查询

```mongodb

> db.articles.find({$text:{$search:"aa"}},{score:{$meta:"textScore"}})
{ "_id" : ObjectId("5a337255f4884d2e66da1231"), "content" : "aa bb cc dd ee", "score" : 0.6 }
{ "_id" : ObjectId("5a337256f4884d2e66da1233"), "content" : "aa bb cc hh dojiofjqjfq", "score" : 0.6 }
{ "_id" : ObjectId("5a337255f4884d2e66da1232"), "content" : "aa bb rr dd", "score" : 0.625 }

#排序
> db.articles.find({$text:{$search:"aa"}},{score:{$meta:"textScore"}}).sort({score:{$meta:"textScore"}})
{ "_id" : ObjectId("5a337255f4884d2e66da1232"), "content" : "aa bb rr dd", "score" : 0.625 }
{ "_id" : ObjectId("5a337255f4884d2e66da1231"), "content" : "aa bb cc dd ee", "score" : 0.6 }
{ "_id" : ObjectId("5a337256f4884d2e66da1233"), "content" : "aa bb cc hh dojiofjqjfq", "score" : 0.6 }
```

# 自定义索引

## name指定

```mongodb

> db.articles.ensureIndex({num:1},{name:"num_index"})
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 2,
	"numIndexesAfter" : 3,
	"ok" : 1
}

> db.articles.getIndexes()
[
	{
		"v" : 2,
		"key" : {
			"num" : 1
		},
		"name" : "num_index",
		"ns" : "vding.articles"
	}
]
```

## unique指定

```mongodb

db.test.insert({num:20})

> db.test.ensureIndex({num:1},{unique:true})
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}


> db.test.getIndexes()
[
	{
		"v" : 2,
		"key" : {
			"_id" : 1
		},
		"name" : "_id_",
		"ns" : "vding.test"
	},
	{
		"v" : 2,
		"unique" : true,
		"key" : {
			"num" : 1
		},
		"name" : "num_1",
		"ns" : "vding.test"
	}
]


> db.test.insert({num:20})
WriteResult({
	"nInserted" : 0,
	"writeError" : {
		"code" : 11000,
		"errmsg" : "E11000 duplicate key error collection: vding.test index: num_1 dup key: { : 20.0 }"
	}
})


```


## sparse和expireAfterSeconds指定

```

6-3 [mongoDB] 索引属性—sparse和expireAfterSeconds指定 (0453)

默认创建索引是不稀疏
稀疏好处 对不存在的数据,不创建索引

#稀疏性,spare指定 格式 
db.collection.ensureIndex({},{spare:true/false})

#插入两个数据
>use imooc
>db.imooc_2.insert({"m":1})
>db.imooc_2.insert({"n":1})
>db.imooc_2.find({m:{$exists:true}})  # 返回 "m":1一条数据

>db.imooc_2.ensureIndex({m:1},{sparse:true}) #设置稀疏性

>db.imooc_2.find({m:{$exists:false}}) # 返回 "n":1一条数据

>db.imooc_2.getIndexes()   #查看索引情况

{
	"v":1,
	"key":{
		"m":1
	},
	"name":"m_1",
	"ns":"imooc.imooc_2",
	"sparse":true
}

>db.imooc_2.find({m:{$exists:false}}).hint("m_1")  #强制使用索引  没有数据输出,达到预期的目标,没有数据,则没有索引

#是否定时删除,expireAfterSeconds指定:
	TTL,过期索引


```

# 查询方式:

## $near查询

```
> use vding

> db.location.insert({position:[1,1]})
> db.location.insert({position:[1,2]})
> db.location.insert({position:[3,2]})
> db.location.insert({position:[100,100]})
> db.location.insert({position:[180,100]})

# 取值范围:经度[-180,180] 续度[-90,90],否则会出错
> db.location.remove({position:[100,100]})
> db.location.remove({position:[180,100]})

#未添加索引查询会报错 
> db.location.find({position:{$near:[1,1]}})
Error: error: {
	"ok" : 0,
	"errmsg" : "error processing query: ns=vding.locationTree: GEONEAR  field=position maxdist=1.79769e+308 isNearSphere=0\nSort: {}\nProj: {}\n planner returned error: unable to find index for $geoNear query",
	"code" : 2,
	"codeName" : "BadValue"
}

# 添加2d索引
> db.location.ensureIndex({position:"2d"})
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}

# 查询出来
> db.location.find({position:{$near:[1,1]}})
{ "_id" : ObjectId("5a372a17c693146bd892b1d9"), "position" : [ 1, 1 ] }
{ "_id" : ObjectId("5a372a1bc693146bd892b1da"), "position" : [ 1, 2 ] }
{ "_id" : ObjectId("5a372a1ec693146bd892b1db"), "position" : [ 3, 2 ] }


#距离我最远10
> db.location.find({position:{$near:[1,1],$maxDistance:10}})
{ "_id" : ObjectId("5a372a17c693146bd892b1d9"), "position" : [ 1, 1 ] }
{ "_id" : ObjectId("5a372a1bc693146bd892b1da"), "position" : [ 1, 2 ] }
{ "_id" : ObjectId("5a372a1ec693146bd892b1db"), "position" : [ 3, 2 ] }
> 
#不支持$minDistance
> db.location.find({position:{$near:[1,1],$maxDistance:10,$minDistance:3}}) #minDistance不起作用
> 
```

## $geoWithin查询

```
#$box演示

use imooc
db.location.find({w:{$geoWithin:{$box:[[0,0],[3,3]]}}})
db.location.find({w:{$geoWithin:{$box:[[1,1],[2,3]]}}})


#$center演示
db.location.find({w:{$geoWithin:{#$center演示:[[0,0,5]}}})
 
#$polygon演示
db.location.find({w:{$geoWithin:{$polygon:[[0,0],[0,1],[2,5],[6,1]]}}})


> db.location.find({position:{$geoWithin:{$box:[[0,0],[3,3]]}}})
{ "_id" : ObjectId("5a372a17c693146bd892b1d9"), "position" : [ 1, 1 ] }
{ "_id" : ObjectId("5a372a1bc693146bd892b1da"), "position" : [ 1, 2 ] }
{ "_id" : ObjectId("5a372a1ec693146bd892b1db"), "position" : [ 3, 2 ] }

```

## 使用geoNear查询

```

geoNear使用runCommand命令进行使用,常用使用如下:
db.runCommand(
	{geoNear:<collection>,
	near:[x,y],
	minDistance:(对2d索引无效)
	maxDistance:
	num:
	}
)

> db.runCommand({geoNear:"location",near:[1,2],maxDistance:10,num:1})
{
	"results" : [
		{
			"dis" : 0,
			"obj" : {
				"_id" : ObjectId("5a372a1bc693146bd892b1da"),
				"position" : [
					1,
					2
				]
			}
		}
	],
	"stats" : {
		"nscanned" : 3,
		"objectsLoaded" : 1,
		"avgDistance" : 0,
		"maxDistance" : 0,
		"time" : 418
	},
	"ok" : 1
}
```


## 使用mongostat效果验证

```

6-11 使用mongostat效果验证 (0252)


#终端A

./bin/mongo 127.0.0.1:12345

> use imooc
>for(i=0;i<10000;i++)db.imooc_2.insert({x:i})  #批量插入1万条数据


#终端B
./bin/mongostat -h 127.0.0.1:12345
```


## profile集合介绍

```
6-12 关于profile集合 (0651)

db.getProfilingStatus()
#输出 {"was":2,"slowns":1}
db.getProfilingLevel()  #分为3个级别  0为关闭,mongo不记录  1为mongo会记录slowns超过该值的记录   2.mongo记录任何操作

db.setProfilingLevel(2) #设置级别


show tables #会有一项system.profile

db.system.profile.find()  #查看profile
db.system.profile.find().sort({$natural:-1}).limit(10) #降序查看 
```


## 日志介绍

```
vim conf/mongod.conf

port=12345
dbpath=data
logpath=log/mongod.log
bind_ip=127.0.0.1
verbose = vvvvv  #位数越长,越详细
fork=true
```

## explain分析

```
db.imooc_2.find({x:1}).explain()

{
      ...
	"millis":112
      ...
}

db.imooc_2.ensureIndex({x:1})  #建立一个索引


 db.imooc_2.find({x:100}).explain()
{
      ...
	"millis":26  #建立了索引之后,这个时间缩短啦
      ...
}

```


## 开启权限认证

**2.6.5**
```
vim conf/mongod.conf
port=12345
dbpath=data
logpath=log/mongod.log
bind_ip=127.0.0.1
verbose = vvvvv  #位数越长,越详细
fork=true
auth=true

ps -ef | grep mongod|grep 12345
kill 9528


重启启动服务

./bin/mongod --port 12345 --dbpath ./data/ --logpath ./log/mongod.log --fork -f conf/mongod.conf

cat log/mongod.log  #查找一下 auth 

 
 ./bin/mongo 127.0.0.1:12345  #发现还可以进入,是因为还没有创建用户

```

**3.2.4**

```


```


## 创建用户

```
## > db.createUser({user:"admin",pwd:"admin",roles:[{role:"userAdmin",db:"vding"},{role:"read",db:"test"}]})
Successfully added user: {
	"user" : "admin",
	"roles" : [
		{
			"role" : "userAdmin",
			"db" : "vding"
		},
		{
			"role" : "read",
			"db" : "test"
		}
	]
}

```

## 删除用户

```
> show users
{
	"_id" : "test.admin",
	"user" : "admin",
	"db" : "test",
	"roles" : [
		{
			"role" : "userAdmin",
			"db" : "vding"
		},
		{
			"role" : "read",
			"db" : "test"
		}
	]
}

# 方法1
> use test;
switched to db test
> db.dropUser("admin")
true

# 方法2
db.runCommand( { dropUser: "admin" } )
```

## 2.6.5配置mongod.conf

```
auth=true
```

## 3.2.4配置mongod.conf

```
security:
  authorization:  enabled
```