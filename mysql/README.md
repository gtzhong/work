# mysql

- 常用功能
	- 时间戳转与日期转换
		- select FROM_UNIXTIME(1156219870);
		- Select UNIX_TIMESTAMP(’2006-11-04 12:23:00′);
		- SELECT DATE_FORMAT(FROM_UNIXTIME(1499415050),'%Y-%m-%d')  //时间翠转换为日期
	- 转换类型	
		- CONVERT(xxx,类型) 或 CAST(xxx AS 类型)
			- cast(a as signed) 	//varchar转Int
			- concat(8,’0′) 		//Int转为varcha
			- 类型
				- 二进制,同带binary前缀的效果 : BINARY
				- 字符型,可带参数 : CHAR()
				- 日期 : DATE
				- 时间: TIME
				- 日期时间型 : DATETIME
				- 浮点数 : DECIMAL
				- 整数 : SIGNED
				- 无符号整数 : UNSIGNED
			- 举例
				- select cast(‘125e342.83’ as signed) as clm1		//转换正型
		- 将字符串转化为数字类型存储
			- SELECT INET_ATON('192.168.2.10')  //输出 3232236042  //将IP转化为数字
			- SELECT INET_NTOA(3232236042) //192.168.2.10   //将数字转化为IP
	- SQL设计开发规范 @sqlercn 
		- 非负数的字段尽量使用无符号整形
		- 避免使用TEXT,BLOG和ENUM类型
		- 尽可能把所有列定义为NOT NULL
		- 使用TIMESTAMP或DATETIME类型存储时间
		- 金融类数据,必须使用decimal类型
		- 避免使用双%号查询条件,如 %123% . 使用后置 正确使用 123%
		- 一个SQL只能利用到复合索引中的一列进行范围查询 如 a b c 做为复合索引,a列是做范围查询的,则应该放在右侧
		- 使用left join 或 no exists来优化 not in操作
		- 程序连接不同的数据库使用不同的帐号,禁止跨库查询
		- 禁止使用不含字段列表的insert语句
			- insert into t values('a','b','c')  不建议
			- insert into t(c1,c2,c3) values('a','b','c') 推荐做法
		- 避免使用子查询,可以把子查询优化为join操作
		- 避免使用JOIN关联太多的表 Mysql最多允许关联61个表,建议不超过5个 
		- 使用in 代替 or
			- in的值不要超过500个
			- in操作可以有效利用索引
		- 禁止使用 order by rand() 进行随机排序
		- where 从句中禁止对列进行函数转换和计算(会导致无法使用索引)
			- where date(createtime) = '20160901'  不建议
			- where dcreatetime >= '20160901'  and createtime < '20160902'
		- 在明显不会有重复值时使用UNION ALL 而不是UNION
			- UNION会把所有数据放到临时表中再进行去操操作
			- UNION ALL不会再对结果集进行去重操作
		- 拆分复杂的大SQL为多个小SQL
			- 一个SQL只能使用一个CPU进行计算
			- SQL拆分后可能通过并行执行来提高处理效率
	- SQL操作行为规范
		- 超100万行的批量写操作,要分批多次进行操作
		- 对于大表使用 pt-online-schema-change 修改表结构
			- 避免大表修改产生的主从延迟
			- 避免在对表字段进行修改时进行锁表
		- 禁止为程序使用帐号赋予super权限
			- 当达到最大连接数限制时,还允许1个有super权限的用户连接
			- super权限只能留给DBA处理问题的帐号使用
		- 对于程序连接数据库帐号,遵循权限最小原则 
			- 程序使用数据库帐号只能在一个DB下使用,不准跨库
			- 程序使用的账号原则上不准有drop权限
	- 批量查询表的记录数量
		- use information_schema

			```
			SELECT CONCAT(
			    'select "', 
			    TABLE_name, 
			    '", count(*) from ', 
			    TABLE_SCHEMA, 
			    '.',
			    TABLE_name,
			    ' union all'
			) FROM TABLES 
			WHERE TABLE_SCHEMA='数据库名';
			```
	- in 和 FIND_IN_SET(代替in)
		- id in(1,2,3) 或 name in ('a','b','c')
		- find_in_set(id,'a,b,c')
		- instr 这个会出现间接的失效 
	- 1=1妙用
		- AND IF(_which_day !='0000-00-00', dj_checklist.which_date = _which_day, '1=1') 
	- if巧用
		- if(mp_pricelist.original_product_id IS NULL,(if(mp_order.transaction_status!=13,mp_order_detail.quantity,0)),mp_order_detail.quantity)
	- ifnull巧用
		- (SELECT ifnull(SUM(mp_order_detail.quantity),0)  FROM mp_order_detail LEFT JOIN mp_order _mp_order ON _mp_order.id = mp_order_detail.order_id WHERE mp_order_detail.original_product_id = {$product_id} AND mp_order_detail.product_model_id !=3 AND mp_order_detail.product_id != mp_order_detail.original_product_id   AND _mp_order.used_day =  mp_order.used_day)
	- 动态执行sql

		```
		BEGIN
		 SET @sql = concat('select * from ', $tableName);	 
		 PREPARE stmt1 FROM @sql;
		 EXECUTE stmt1;
		 DEALLOCATE PREPARE stmt1;
		END;
		```
   - 子查询 [子查询的好处就是  如果子条件不符合，父记录。。也会存在（传统的情况下，父记录是不存在的）]

		```
		left join (SELECT Amount,CreateTime,LoanId FROM invest WHERE IsValid = 1 AND invest.TransferFlag != 3) AS invest 
		```
	- between 
		- 字符串判断是否在范围内
		```mysql
        //例a
		SELECT 'b' BETWEEN 'a' AND 'c'
		
		//例b
		SELECT * FROM user WHERE username BETWEEN 'a' AND 'k'
		```
		- 数字判断是否在范围内
		```mysql
		//1.例a
		SELECT 3 BETWEEN 2 AND 5

		//2.例b
		IF !(SELECT UNIX_TIMESTAMP(NOW()) BETWEEN _play_start_at AND _play_end_at) THEN 
			SELECT '-5' AS 'id','不在有效期内' AS 'note';  
			LEAVE label_break; -- 返回并终止进行  
		END IF;
		
		//3.其它
		SELECT * FROM user WHERE uid BETWEEN 2 AND 5
		```
	- date_add
		- x
	- function函数
		- [循环DECLARE cur_1 CURSOR再运行操作](fn/function/function_循环DECLARE_cur_1_CURSOR再运行操作.sql)
	- 找回密码
	  - 方法1
		  - 在 [mysqld]  加入 skip_grant_tables
		  - 重启,mysql -uroot -p //即可进入
	  - 方法2
		  -  mysqld_safe --skip-grant-tables&
	  - 方法3
		  - mysqld_safe –skip-grant-tables &
		  - mysqld_safe --skip-grant-tables >/dev/null 2>&1 &
	- 创建用户与授权
	  - insert into user(host,user,password) values('%','root',password('!123456'));  //创建一个帐号
	  - update mysql.user set password=password('123456') where User='root'; //root重置密码
	  - grant all privileges on `*.*` to root@"%";  //允许远程连接
	  - grant all privileges on `*.*` to 'bitnami'@'%' identified by 'a4f90127b5'; （bitnami 为用户名，a4f90127b5 为密码） 
	  - FLUSH PRIVILEGES; 
	- SELECT @@VERSION;  //查看msql版本
	- SELECT CONNECTION_ID(); //获取当前用户登陆的连接ID
- 配置文件 my.cnf
	- 仅允许本地127.0.0.1连接
		- [mysqld] bind-address=127.0.0.1
	- 修改数据库,不使用密码
		- [mysqld] skip_grant_tables
	-如果"导出"出现问题,有可能是太大了
		- max_allowed_packet = 500M  
- 监控 
	- 监控Innodb的阻塞 
	```
	SELECT
	b.trx_mysql_thread_id AS '被阻塞线路',
	b.trx_query AS '被阻塞SQL',
	c.trx_mysql_thread_id AS '阻塞线程',
	c.trx_query AS '阻塞SQL',
	(UNIX_TIMESTAMP() - UNIX_TIMESTAMP(c.trx_started)) AS '阻塞时间' 
	FROM information_schema.INNODB_LOCK_WAITS a
	JOIN information_schema.INNODB_TRX b ON a.requesting_trx_id=b.trx_id
	JOIN information_schema.INNODB_TRX c ON a.blocking_trx_id = c.trx_id
	WHERE (UNIX_TIMESTAMP() - UNIX_TIMESTAMP(c.trx_started)) > 60;
	```
- sqlmap @idaxia
	- [sqlmap中文注释](fn/sqlmap/sqlmap中文注释.txt)
	- [python与sqlmap安装](fn/sqlmap/README.md#python与sqlmap安装)
	- [python与sqlmap配置](fn/sqlmap/README.md#python与sqlmap配置)
	- DVWA 构建注入环境
		- [DVWA环境搭建](fn/sqlmap/README.md#DVWA环境搭建)
		- [DVWA配置](fn/sqlmap/README.md#DVWA配置)
		- 操作
			- [sql注入加cookie检测](fn/sqlmap/README.md#sql注入加cookie检测)
			- [以文件方式注入检测](fn/sqlmap/README.md#以文件方式注入检测)  -r
			- [获取数据库](fn/sqlmap/README.md#获取数据库) --dbs
			- [获取当前所有表数据](fn/sqlmap/README.md#获取当前所有表数据)  --dump
			- [选择指定的数据库并导出](fn/sqlmap/README.md#选择指定的数据库并导出) -D
			- [选择指定的表](fn/sqlmap/README.md#选择指定的表) -T 
			- [post注入](fn/sqlmap/README.md#post注入)
			- [忽略老提示](fn/sqlmap/README.md#忽略老提示) --batch --smart
			- [批量处理以文件形式注入](fn/sqlmap/README.md#批量处理以文件形式注入)
			- [寻找注入点](fn/sqlmap/README.md#寻找注入点)	sqlmap.py -g "inurl:\".php?id=1\"" 
		- 如何防范sql注入
			- WEB防火墙
				- [ngx_lua_waf](https://github.com/loveshell/ngx_lua_waf)
				- [ngx_lua_waf效果显示](fn/sqlmap/README.md#ngx_lua_waf效果显示)
			- 开发者需要注意过滤 
- 搜索text类型内容
```php
	if (!$hasPushed) {
		$searchQuery = '%' . str_replace(' ', '%', $keywords) . '%';
		/** 搜索无法进入隐私项保护归档 */
		$select->where('table.contents.password IS NULL')
		->where('table.contents.title LIKE ? OR table.contents.text LIKE ?', $searchQuery, $searchQuery)
		->where('table.contents.type = ?', 'post');
	}
```