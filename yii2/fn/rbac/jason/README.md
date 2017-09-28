# RBAC慕课开发平台

## 配置文件

**源代码**  
[web.php](https://github.com/408824338/yii2_Jason/blob/master/config/web.php)   

**yii2_Jason/config/web.php**
```php
'components' => [
    'authManager' => [
        'class' => 'yii\rbac\DbManager',
        // auth_item (role permission)
        // auth_item_child (role->permission)
        // auth_assignment (user->role)
        // auth_rule (rule)
        'itemTable' => '{{%auth_item}}',
        'itemChildTable' => '{{%auth_item_child}}',
        'assignmentTable' => '{{%auth_assignment}}',
        'ruleTable' => '{{%auth_rule}}',
        'defaultRoles' => ['default'],
    ],
]
```

## 生成权限表

**源代码**  
[console.php](https://github.com/408824338/yii2_Jason/blob/master/config/console.php)  

### 配置console

**yii2_Jason/config/console.php**
```php
$config = [
    'components' => [
        'authManager' => [
            'class' => 'yii\rbac\DbManager',
            // auth_item (role permission)
            // auth_item_child (role->permission)
            // auth_assignment (user->role)
            // auth_rule (rule)
            'itemTable' => '{{%auth_item}}',
            'itemChildTable' => '{{%auth_item_child}}',
            'assignmentTable' => '{{%auth_assignment}}',
            'ruleTable' => '{{%auth_rule}}',
        ],
    ]
]
```

### 运行yii生成

**网站根目录执行**
```php
./yii migrate --migrationPath=@yii/rbac/migrations
```


## 创建角色

**源代码**  
[RbacController.php](https://github.com/408824338/yii2_Jason/blob/master/modules/controllers/RbacController.php)  
[__createitem.php](https://github.com/408824338/yii2_Jason/blob/master/modules/views/rbac/_createitem.php)  视图文件  

![](images/create_role.png)

**yii2_Jason/modules/controllers/RbacController.php**

```php
namespace app\modules\controllers;
use Yii;
use \yii\data\ActiveDataProvider;
use \yii\db\Query;
use app\modules\models\Rbac;
class RbacController extends CommonController
{
    public $mustlogin = ['createrule', 'createrole', 'roles', 'assignitem'];
    public function actionCreaterole()
    {
        if (Yii::$app->request->isPost) {
            $auth = Yii::$app->authManager;
            $role = $auth->createRole(null);
            $post = Yii::$app->request->post();
            if (empty($post['name']) || empty($post['description'])) {
                throw new \Exception('参数错误');
            }
            $role->name = $post['name'];
            $role->description = $post['description'];
            $role->ruleName = empty($post['rule_name']) ? null : $post['rule_name'];
            $role->data = empty($post['data']) ? null : $post['data'];
            if ($auth->add($role)) {
                Yii::$app->session->setFlash('info', '添加成功');
            }
        }
        return $this->render('_createitem');
    }
}    
```