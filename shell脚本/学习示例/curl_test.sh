#!/bin/bash
num=0
#文件由windows生成，需要转换格式，方式如下：
#命令dos2unix test.file
#去掉"\r" ，用命令sed -i ""s/\r//"" test.file
for url in `cat cdn.txt`
 
do
  num=$((${num}+1)) #运算需要加双层括号

   result_code=`curl -I -H "Host:dl.liebao.cn" -o /dev/null -s -w %{http_code}  ${url}`
#-o /dev/null 屏蔽原有输出信息
#-s silent 模式，不输出任何东西
#-w %{http_code} 控制额外输出

   echo $num; 
   echo $url,$result_code >> result.txt
done
