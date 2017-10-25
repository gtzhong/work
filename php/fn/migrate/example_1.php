<?php
/*
简单的一对一两库操作
*/
$CONFIG['TTLSA']['from'] = array();
$CONFIG['TTLSA']['from']['db_user'] = 'root';
$CONFIG['TTLSA']['from']['db_pass'] = '123456';
$CONFIG['TTLSA']['from']['db_name'] = 'ttlsa';
$CONFIG['TTLSA']['from']['db_host'] = "192.168.1.2";

$CONFIG['TTLSA']['to'] = array();
$CONFIG['TTLSA']['to']['db_user'] = 'root';
$CONFIG['TTLSA']['to']['db_pass'] = '';
$CONFIG['TTLSA']['to']['db_name'] = 'ttlsa_blog';
$CONFIG['TTLSA']['to']['db_host'] = "localhost";

$from_conn = mysql_connect($CONFIG['TTLSA']['from']['db_host'], $CONFIG['TTLSA']['from']['db_user'], $CONFIG['TTLSA']['from']['db_pass'], $CONFIG['TTLSA']['from']['db_name']);
$to_conn = mysql_connect($CONFIG['TTLSA']['to']['db_host'], $CONFIG['TTLSA']['to']['db_user'], $CONFIG['TTLSA']['to']['db_pass']);
mysql_select_db($CONFIG['TTLSA']['from']['db_name'], $from_conn);
$max = 3000000;
$step = 100000;
for ($i = 1; $step_i = $i + $step;$max++) {
    mysql_query("set names 'utf8'", $from_conn);
    $sql = "select uid,reg_ip,reg_time,last_login,question,answer from users where user_id>=$i and user_id";

    $rs = mysql_query($sql, $from_conn) or die("Invalid query: " . mysql_error());

    $value = array();
    while ($v = mysql_fetch_array($rs, MYSQL_ASSOC)) {
        $column = array();
        $column['uid'] = $v['uid'];
        $column['reg_ip'] = $v['reg_ip'];
        $column['reg_time'] = $v['reg_time'];
        $column['last_login'] = $v['last_login'];
        if ($column['question'] && $column['answer']) {
            $column['aq'] = serialize(array($v['question'], $v['answer'])); //序列化存储
        } else {
            $column['aq'] = '';
        }
        $value[] .= "('{$column['uid']}','{$column['reg_ip']}','{$column['reg_time']}','{$column['last_login']}','{$column['aq']}')";
    }
    if ($value) {
        $sql = "insert into ttlsa_users(uid, reg_ip, reg_time, last_login, aq) values " . implode(",", $value);
        mysql_select_db($CONFIG['TTLSA']['to']['db_name'], $to_conn);
        mysql_query("set names 'utf8'", $to_conn);
        mysql_query($sql, $to_conn) or die("Invalid query: " . mysql_error());
    }
}
?>