# 过滤器AccessControl和VerbFilter及全局设置

**源代码**  
[CommonController.php](https://github.com/408824338/yii2_Jason/blob/master/controllers/CommonController.php)  
[OrderController.php](https://github.com/408824338/yii2_Jason/blob/master/controllers/OrderController.php)

## CommonController定义

**yii2_Jason/controllers/CommonController.php**
```php

class CommonController extends Controller
{

    protected $actions = ['*'];
    protected $except = [];
    protected $mustlogin = [];
    protected $verbs = [];

    public function behaviors()
    {
        return [
            'access' => [
                'class' => \yii\filters\AccessControl::className(),
                'only' => $this->actions,
                'except' => $this->except,
                'rules' => [
                    [
                        'allow' => false,
                        'actions' => empty($this->mustlogin) ? [] : $this->mustlogin,
                        'roles' => ['?'], // guest
                    ],
                    [
                        'allow' => true,
                        'actions' => empty($this->mustlogin) ? [] : $this->mustlogin,
                        'roles' => ['@'], //已经登陆
                    ],
                ],
            ],
            'verbs' => [
                'class' => \yii\filters\VerbFilter::className(),
                'actions' => $this->verbs,
            ],
        ];
    }

}
```

## 普通控制器设置过滤

**yii2_Jason/controllers/OrderController.php**
```php

class OrderController extends CommonController
{

    //定义哪些是要验证
    protected $mustlogin = ['index', 'check', 'add', 'confirm', 'pay', 'getexpress', 'received'];

    //指定actionConfirm()方法必须使用post提交
    protected $verbs = [
        'confirm' => ['post']
    ];

    ...
}    
```

## 后台设置全局filter过滤器和verbFilter

**源代码**  
[CommonController.php]
(https://github.com/408824338/yii2_Jason/blob/master/modules/controllers/CommonController.php)  

**yii2_Jason/config/web.php**

```php
'components' => [
        'admin' => [
            'class' => 'yii\web\User',
            'identityClass' => 'app\modules\models\Admin',
            'idParam' => '__admin',
            'identityCookie' => ['name' => '__admin_identity', 'httpOnly' => true],
            'enableAutoLogin' => true,
            'loginUrl' => ['/admin/public/login'],
        ],
]        
```

**yii2_Jason/modules/controllers/CommonController.php**

```php
class CommonController extends Controller
{
    public $layout = 'layout1';
    protected $actions = ['*'];
    protected $except = [];
    protected $mustlogin = [];
    public function behaviors()
    {
        return [
            'access' => [
                'class' => \yii\filters\AccessControl::className(),
                'user' => 'admin',  //注: 因为web.php配置 admin自定义user类型,如上 
                'only' => $this->actions,
                'except' => $this->except,
                'rules' => [
                    [
                        'allow' => false,
                        'actions' => empty($this->mustlogin) ? [] : $this->mustlogin,
                        'roles' => ['?'],
                    ],
                    [
                        'allow' => true,
                        'actions' => empty($this->mustlogin) ? [] : $this->mustlogin,
                        'roles' => ['@'],
                    ],
                ],
            ],
        ];
    }
}    
```