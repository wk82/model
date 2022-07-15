#!/bin/bash
#输入数字
read -p "input your number:" numb1
#判断数字
numb_check=$(echo ${numb1}|grep "^[0-9]\{1,\}")
if [ "${numb_check}" == "" ];then
   echo "input wrong number"
   exit 1
fi

s=0
for ((i=0;i<=${numb1};i=i+1))
do 
   s=$((${s}+${i}))
done
   echo "result is ${s}"
