# 模仿慕课开发平台

## 实现前后端登陆配置

**源代码**  
[web.php](https://github.com/408824338/yii2_Jason/blob/master/config/web.php)  

```php
'components' => [
    'user' => [
        'identityClass' => 'app\models\User',
        'enableAutoLogin' => true,
        'idParam' => '__user',
        'identityCookie' => ['name' => '__user_identity', 'httpOnly' => true],
        'loginUrl' => ['/member/auth'],
    ],
    'admin' => [
        'class' => 'yii\web\User',
        'identityClass' => 'app\modules\models\Admin',
        'idParam' => '__admin',
        'identityCookie' => ['name' => '__admin_identity', 'httpOnly' => true],
        'enableAutoLogin' => true,
        'loginUrl' => ['/admin/public/login'],
    ]
]
```

## 前台登陆与退出

**源代码**   
[MemberController.php](https://github.com/408824338/yii2_Jason/blob/master/controllers/MemberController.php)  

**/yii2_Jason/controllers/MemberController.php**

```php
<?php
namespace app\controllers;
use app\controllers\CommonController;
use app\models\User;
use Yii;
class MemberController extends CommonController
{
    //登陆
     public function actionAuth()
    {
        $this->layout = 'layout2';
        if (Yii::$app->request->isGet) {
            $url = Yii::$app->request->referrer;
            if (empty($url)) {
                $url = "/";
            }
            Yii::$app->session->setFlash('referrer', $url);
        }
        $model = new User;
        if (Yii::$app->request->isPost) {
            $post = Yii::$app->request->post();
            if ($model->login($post)) {
                $url = Yii::$app->session->getFlash('referrer');
                return $this->redirect($url);
            }
        }
        return $this->render("auth", ['model' => $model]);
    }

    //退出
     public function actionLogout()
    {   
        Yii::$app->user->logout(false); //必须带上false参数,否则前后台同时退出
        return $this->goBack(Yii::$app->request->referrer);
    }
}    
```

## 后台登陆与退出
**源代码**  
[UserController.php](https://github.com/408824338/yii2_Jason/blob/master/modules/controllers/UserController.php)  

**yii2_Jason/modules/controllers/UserController.php**

```php
<?php
namespace app\modules\controllers;
use yii\web\Controller;
use app\modules\models\Admin;
use Yii;
class PublicController extends Controller
{
    //登录
    public function actionLogin()
    {
        $this->layout = false;
        $model = new Admin;
        if (Yii::$app->request->isPost) {
            $post = Yii::$app->request->post();
            if ($model->login($post)) {
                $this->redirect(['default/index']);
                Yii::$app->end();
            }
        }
        return $this->render("login", ['model' => $model]);
    }

    //退出
    public function actionLogout()
    {
        Yii::$app->admin->logout(false);//必须带上false参数,否则前后台同时退出
        return $this->goback();
    }
}    
```

## bcrypt密码加密

**生成bcrypt密码**

```php
Yii::$app->getSecurity()->generatePasswordHash($password);
```

**输入的密码和数据库密码比较**

```php
Yii::$app->getSecurity()->validatePassword($input_pass,$db_pass);
```

```php

    //密码生比较
    public function validatePass()
    {
        if (!$this->hasErrors()) {
            $loginname = "username";
            if (preg_match('/@/', $this->loginname)) {
                $loginname = "useremail";
            }
            $data = self::find()->where($loginname.' = :loginname', [':loginname' => $this->loginname])->one();
            if (is_null($data)) {
                $this->addError("userpass", "用户名或者密码错误");
            }
            if (!Yii::$app->getSecurity()->validatePassword($this->userpass, $data->userpass))
            {
                $this->addError("userpass", "用户名或者密码错误");
            }
        }
    }


    //注册时密码生成
    public function reg($data, $scenario = 'reg')
    {
        $this->scenario = $scenario;
        if ($this->load($data) && $this->validate()) {
            $this->createtime = time();
            // $this->userpass = md5($this->userpass);
            $this->userpass = Yii::$app->getSecurity()->generatePasswordHash($this->userpass);
            if ($this->save(false)) {
                return true;
            }
            return false;
        }
        return false;
    }
```


