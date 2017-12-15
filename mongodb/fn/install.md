# 安装

# 2.6.5压缩包安装

```linux

MongoDB环境 : 64位linux
MongoDB版本: 2.6.5
ssh工具 : xshell
文本编辑器: vim 与 notepad++


2-2 编译mongoDB文件 (0305)

# 安装
> ls
mongo-r.2.6.5.zip  mongo-r2.6.5
> cd mongo-r2.6.5
> scons all -j 12

2-3 搭建简单的mongoDB服务器 (0354)


mkdir mongodb_simple
cd mongodb_simple
mkdir data
mkdir log
mkdir conf
mkdir bin
cp ../mongo-r2.6.5/mongod bin/
cp ../mongo-r2.6.5/mongo bin/   #连接的客户端
cd conf
vim mongod.conf


vim mongod.conf内容如下

port = 12345
dbpath = data
logpath = log/mongod.log
fork = true

#启动
cd mongodb_simple
./bin/mongod -f conf/mongod.conf

```


## 3.2.4yum安装
[官网安装流程](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)

```shell
touch /etc/yum.repos.d/mongodb-org-3.6.repo

#内容如下
[mongodb-org-3.6]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.6/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc


yum install -y mongodb-org

```