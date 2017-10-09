
# url美化

##路由设置-伪静态

>例1
>访问地址： http://url/coshop/60   
>等同于访问 http://url/coshop/default/index/60/type/4

```php
return [
    'class'=>'yii\web\UrlManager',
    'enablePrettyUrl'=>true,
    'showScriptName'=>false,
    'rules'=>[
        // url rules
        [
            'pattern' => 'coshop/<shop_id:\d+>/<type:\d+>',
            'route' => 'coshop/default/index',
            'defaults' => ['type' => 4],
        ],
    ]
];
```

# 案例@Jason

源代码

**URl配置信息**

```php
'components' => [
        'urlManager' => [
            'enablePrettyUrl' => true,
            'showScriptName' => false,
            'suffix' => '.html',
            'rules' => [
                '<controller:(index|cart|order)>' => '<controller>/index',
                'auth' => 'member/auth',  //访问 member/auth 直接跳转到 auth
                'product-category-<cateid:\d+>' => 'product/index',
                'product-<productid:\d+>' => 'product/detail',
                'order-check-<orderid:\d+>' => 'order/check',
                [
                    'pattern' => 'imoocback',
                    'route' => '/admin/default/index',
                    'suffix' => '.html',
                ],
            ],
        ],
 ];       

```

## 忽略index方法

```
'<controller:(index|cart|order)>' => '<controller>/index',

访问
http://www.xx..com/index/index
http://www.xx..com/cart/index
http://www.xx..com/order/index

美化
http://www.xx..com/index.html
http://www.xx..com/cart.html
http://www.xx..com/order.html
```

## 分类页伪静态

```
'product-category-<cateid:\d+>' => 'product/index',

http://www.xx..com/product/index.html?cateid=20

美化

http://www.xx..com/product-category-20.html

```


## 详情页伪静态 

```
'product-<productid:\d+>' => 'product/detail',

http://www.xx..com/product/detail.html?productid=7

美化

http://www.xx..com/product-7.html

```

## 购物车伪静态

```
'order-check-<orderid:\d+>' => 'order/check',

http://www.xx..com/order/check.html?orderid=20

美化

http://www.xx..com/order-check-20.html
```

## 后台登陆地址伪静态

```
 [
    'pattern' => 'imoocback',
    'route' => '/admin/default/index',
    'suffix' => '.html',
 ],

 http://www.xx..com/imoocback.html

 跳转

  http://www.xx..com/admin/default/index.html
 

```