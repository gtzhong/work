<?php

#Connection variables :
$mysql_host = '';
$mysql_user = '';
$mysql_password = '';
$mysql_database = '';
$mysql_link = mysql_connect(
  $mysql_host,
  $mysql_user,
  $mysql_password);

$mssql_host = '';
$mssql_user = '';
$mssql_password = '';
$mssql_database = '';
$mssql_link = mssql_connect(
  $mssql_host,
  $mssql_user,
  $mssql_password);

$tables = array(/* LIST THE TABLES YOU WANT TO MIGRATE HERE */);

#Select the databases:
mysql_select_db($mysql_database);
mssql_select_db($mssql_database);

#Migrate the data:
foreach($tables as $table){

  $m_res = mssql_query('select * from '. $table);

  $j = 0;

  while($rec = mssql_fetch_array($m_res, MSSQL_NUM)){
      echo $table, ' >> ', $j++, "\n";
      $cols = count($rec);
      for($i = 0; $i < $cols; $i++){
          if(is_string($rec[$i])){
              $rec[$i] = "'" . mysql_real_escape_string($rec[$i]) . "'";
          }
          if(is_null($rec[$i])) $rec[$i] = 'NULL';
      }

      $query = 'insert into '.$table." values (" . implode(",", $rec) . ");";
      $res = mysql_query($query);
      if(!$res) echo $query, ' >>>>>>>>> ', mysql_error(), "\n";
  }

}