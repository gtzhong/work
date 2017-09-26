//连接本地的 Redis 服务
$redis = new \Redis();
$redis->connect('r-wz9b3a4d3f7071b4.redis.rds.aliyuncs.com', 6379);
//验证服务
$redis->auth('5316de60A3cab6x49');
//选择连接库
$redis->select(1);
//查看服务是否运行
$keysList = $redis->keys("*");