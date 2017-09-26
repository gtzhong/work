# 前端开发
## 前端提交获取csrf相关参数
**可以参考下面调用的例子**
```php
$csrfvar = Yii::$app->request->csrfParam;
$csrfval = Yii::$app->request->getCsrfToken();
    var postData = {
        '$csrfvar' : '$csrfval',
        'new' : newtext,
        'old' : old,
        'id' : id
    };
```

## view页面js使用
**某前端页面**
```php
<?php
$rename = yii\helpers\Url::to(['category/rename']);
$delete = yii\helpers\Url::to(['category/delete']);
$csrfvar = Yii::$app->request->csrfParam;
$csrfval = Yii::$app->request->getCsrfToken();
$js = <<<JS
$("#w0").on("rename_node.jstree", function(e, data){
    var newtext = data.text;
    var old = data.old;
    var id = data.node.id;
    var postData = {
        '$csrfvar' : '$csrfval',
        'new' : newtext,
        'old' : old,
        'id' : id
    };
    $.post('$rename', postData, function(data) {
        if (data.code != 0) {
            alert('修改失败');
            window.location.reload();
        }
    });
}).on("delete_node.jstree", function(e, data){
    var id = data.node.id;
    $.get('$delete', {id: id}, function(data){
        if (data.code != 0) {
            alert('删除失败:'+data.message);
            window.location.reload();
        }
    });
})
JS;
$this->registerJs($js);
?>
```

## 根据环境加载是否压缩的js和css
**web.php配置文件**
```php
    'components' => [
        'assetManager' => [
            'class' => 'yii\web\AssetManager',
            'bundles' => [
                'yii\web\JqueryAsset' => [
                    'js' => [
                        YII_ENV_DEV ? 'jquery.js' : 'jquery.min.js'
                    ],
                ],
                'yii\bootstrap\BootstrapAsset' => [
                    'css' => [
                        YII_ENV_DEV ? 'css/bootstrap.css' : 'css/bootstrap.min.css',
                    ]
                ],
                'yii\bootstrap\BootstrapPluginAsset' => [
                    'js' => [
                        YII_ENV_DEV ? 'js/bootstrap.js' : 'js/bootstrap.min.js',
                    ]
                ]
            ],
        ],
    ]    
```

