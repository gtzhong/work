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