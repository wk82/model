#!/bin/bash
num=0
for url in `cat cdn.txt`
 
do
  num=$((${num}+1))
  # curl -I -H "Host:dl.liebao.cn" ${url}
   result_code=`curl -I -H "Host:dl.liebao.cn" -o /dev/null -s -w %{http_code}  ${url}`
  #echo $url
   echo $num; 
   echo $url,$result_code >> result.txt
done
