#!/bin/bash
network="192.168.1"
for sitenu in $(seq 1 3) #seq 为sequence(连续)的缩写
do 
   #下面程序取得ping回传值是正确还是失败，正确执行result=0,失败执行result=1
    ping -c 1 -w 1 ${network}.${sitenu} > /dev/null 2>&1 && result=0 || result=1
    if [ "${result}" = 0 ];then
          echo "up"
    else
          echo "down"
    fi
done
