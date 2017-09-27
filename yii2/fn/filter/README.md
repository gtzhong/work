# 过滤器AccessControl和VerbFilter及全局设置

## CommonController定义
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
                        'roles' => ['@'],
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
```php

class OrderController extends CommonController
{

    //定义哪些是要验证
    protected $mustlogin = ['index', 'check', 'add', 'confirm', 'pay', 'getexpress', 'received'];

    //指定actionConfirm()方法必须使用post提交
    protected $verbs = [
        'confirm' => ['post']
    ];

}    
```