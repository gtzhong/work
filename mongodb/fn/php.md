## 版本信息

```
PHP Version 7.0.13
x64
MSVC14 (Visual C++ 2015)
Apache 2.0 Handler
TS,VC14
```

## 扩展与安装

```
#扩展下载
https://pecl.php.net/package/mongodb/1.3.0/windows

#7.0 Thread Safe (TS) x64
http://windows.php.net/downloads/pecl/releases/mongodb/1.3.0/php_mongodb-1.3.0-7.0-ts-vc14-x64.zip

php.ini
extension=php_mongodb.dll

```


## 获取数据

```php
<?php
$mongo = new MongoDB\Driver\Manager("mongodb://vding:123456@192.168.10.33:27017/vding");    // 连接到mongodb
$id           = new \MongoDB\BSON\ObjectId("5a30e53726ca81c5e2bdf583");

//$filter      = ['_id' => $id];
$filter      = [];
$options = [];

$query = new \MongoDB\Driver\Query($filter, $options);
//var_dump($query);exit;
$rows   = $mongo->executeQuery('vding.sms', $query);

foreach ($rows as $document) {
        echo (!empty($document->num) ? $document->num : "") ."  ". (!empty($document->name) ? $document->name:"")."<br />";

}
exit;
?>
```

**输出**

```
1 test
2 test
3 test
4 test
...
```