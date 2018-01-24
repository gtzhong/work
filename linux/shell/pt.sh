#!/bin/bash

# 或关系 查找关键字
# pt -e "(key1)|(key2)"  //或关系 搜索任意关键字
# 使用例子
# pt.sh key1 key2

# 与关系  查找关键字
#  pt -e "(editplus)(正则)"
# 使用例子
# pt.sh and key1 key2


# 获取多个关键字,以空格
_params=$*;

# 切分关键字,以空格切开

OPTS=""


# 与关键字 搜索
if [ "$1" = 'and' ]; then
    var=${_params//,/ }    #这里是将var中的,替换为空格  
    for element in $var   
    do  
        if [ ! $OPTS ]; then
            if [ $element = 'and' ];then
                continue
            else
                 OPTS="$OPTS($element)"
            fi
        else
            OPTS="$OPTS($element)"
        fi
    done  
      result="pt -e \"${OPTS}\""
    
else
# 或关键字 搜索

    var=${_params//,/ }    #这里是将var中的,替换为空格  
    for element in $var   
    do  
        if [ ! $OPTS ]; then
            OPTS="$OPTS($element)"
        else
            OPTS="$OPTS|($element)"
        fi
    done  
    result="pt -e \"${OPTS}\""

fi


#执行
eval $result
