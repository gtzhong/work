# RabbitMQ

## 安装php
sudo apt install php
php -v

## 安装rabbitmq 
sudo apt install rabbitmq-server
ps aux|grep rabbitmq

mkdir sites
cd sites/

## 安装php-amqplib依赖组件 
sudo apt install php-bcmath php-mbstring  php-dom php-curl
sudo apt install composer 

## 下载和更新 php-amqplib  DEMO 
sudo apt install git
git  clone https://github.com/php-amqplib/php-amqplib.git
cd php-amqplib/
composer update 


## 生产者发送消息 
php ~/sites/php-amqplib/demo/amqp_publisher.php message1
-- 消费者接收消息 
php ~/sites/php-amqplib/demo/amqp_consumer.php 


