##输入框选择日期
![](view/input_select_date.png)

```php
        <?php echo $form->field($model, 'to_at', ['options' => ['class' => 'col-lg-2'],])->widget(
            DateTimeWidget::className(), [
                'phpMomentMapping' => ["yyyy-MM-dd HH:mm" => 'YYYY-MM-DD HH:mm',],
                'phpDatetimeFormat' => 'yyyy-MM-dd HH:mm',
                'locale' => 'zh-CN',

            ]
        ) ?>
```

##时间字段年月日显示
![](view/date_format.png)
```php
[  
  'attribute' => '字段名',  
   //'label' => '充值日期',  //强制自定义标题
  'value' => function ($model) {  
   return date('Y-m-d H:i:s', $model->字段名);  
   },  
  //'filter'=>''  //为空，表搜索框隐藏
],  
```

#时间区间范围的选择
![](view/1.DateRangePicker_date_select.png)
>[官方](http://demos.krajee.com/date-range)   
>[composer安装](#安装)    

<br />

>使用  
>[model设置](#model设置)  
>[view设置](#view设置)  


##安装
```
加入composer.json
"kartik-v/yii2-date-range": "*"
 php composer update
```
##model设置
```php
  class UserSearchextendsUser{
	// 1.定义一个变量先
    datapublic $created_at_range; 
		
	  //2.将定义区间名字列入safe
		return ArrayHelper::merge(
			[
				[['created_at_range'], 'safe'] // add a rule to collect the values
			],
			parent::rules()
			);
	}
		
	public functionsearch($params){
		$query = $this->finder->getUserQuery();
		$dataProvider = new ActiveDataProvider(
			[
				'query' => $query,
			]);
		if (!($this->load($params) && $this->validate())) {
			return $dataProvider;
		}
				

		
		//3.获取值
		if(!empty($this->created_at_range) && strpos($this->created_at_range, '-') !== false) {
		    //3.对获取的值，进行切分，赋值要查询两个字段
			list($start_date, $end_date) = explode(' - ', $this->created_at_range);
			$query->andFilterWhere(['between', 'user.created_at', strtotime($start_date), strtotime($end_date)]);
		}		
		// ... more filters here ...return $dataProvider
	}
}

```

##view设置
```php
/* @var $searchModel common\models\UserSearch */// ... lots of code here <?= GridView::widget([
	// ... more code here'columns' => [
		// ... other columns 
		[
                //1.要搜索的字段
                'attribute' => 'created_at',
                // format the value
                'value' => function ($model) {
                    return date('Y-m-d H:i:s', $model->created_at);
                },
                // some styling? 
                'headerOptions' => [
                    'class' => 'col-md-2'
                ],
                //2.保存区间的自定义的字段名
                'filter' => DateRangePicker::widget([
                    'model' => $searchModel,
//                                'language'=>$config['language'],
                    'attribute' => 'created_at_range',
                    'pluginOptions' => [
//				'format' => 'Y-m-d H:i:s',
                        'locale' => [
                            'format' => 'YYYY-MM-DD',
                            'applyLabel' => '确定',
                            'cancelLabel' => '取消',
                            'fromLabel' => '起始时间',
                            'toLabel' => '结束时间',
                            'customRangeLabel' => '自定义',
                            'daysOfWeek' => ['日', '一', '二', '三', '四', '五', '六'],
                            'monthNames' => ['一月', '二月', '三月', '四月', '五月', '六月',
                                '七月', '八月', '九月', '十月', '十一月', '十二月'],
                            'firstDay' => 1
                        ],
                        'autoUpdateInput' => false
                    ]
                ])
            ],
	]
]); ?>
```

##lookup设置