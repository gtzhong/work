# 配置详解

## 配置文件位于config目录中

## elasticsearch.yml


## CRUD实际操作
```
GET _search
{
  "query": {
    "match_all": {}
  }
}


POST /accounts/person/1
{
  "name":"zhang",
  "lostname":"san",
  "desc":"xxxxx"
}



GET accounts/person/1


POST accounts/person/2/_update
{
  "doc":{
     "name":"li",
     "lostname":"si"
  }
 
}


DELETE accounts/person/3
```

# 两种查询形式

## String
```

GET accounts/person/_search
{
  "query": {
    "match": {
      "name": "zhang"
    }
  }
}

```

## DSL

```
GET accounts/person/_search
{
  "query": {
    "term": {
      "name": {
        "value": "zhang"
      }
    }
  }
}

```

## 安装过程遇到问题修改如下配置

```shell
切换到root用户

vi /etc/security/limits.conf

添加如下内容:

* soft nofile 65536

* hard nofile 131072

* soft nproc 2048

* hard nproc 4096

vi /etc/security/limits.d/90-nproc.conf

修改如下内容：

* soft nproc 1024

#修改为

* soft nproc 2048
 

vi /etc/sysctl.conf 

添加下面配置：

vm.max_map_count=655360
并执行命令：

sysctl -p
然后，重新启动elasticsearch，即可启动成功。

#问题:
 system call filters failed to install; check the logs and fix your configuration or disable system call filters at your own risk

#解决:
在elasticsearch.yml中配置bootstrap.system_call_filter为false，注意要在Memory下面:
bootstrap.memory_lock: false
bootstrap.system_call_filter: false

#部分代码如下
# ----------------------------------- Memory -----------------------------------
bootstrap.memory_lock: false
bootstrap.system_call_filter: false


```