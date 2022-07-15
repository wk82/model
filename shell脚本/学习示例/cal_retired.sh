#!/bin/bash
#告知程序用途，并告知如何输入日期格式
echo "this program will try to calculate:"
echo "how many days before you date"
read -p "please input your date (YYYYMMDD ex>20150716):" date2
#测试输入内容是否正确
date_d=$(echo ${date2} | grep '[0-9]\{8\}')  #数字是否有8位
if [ "${date2}" = "" ];then
  echo "you input the wrong format"
exit 1
fi
#开始计算日期
declare -i date_dem=$(date --date="${date2}" +%s)   #退伍日期秒数
declare -i date_now=$(date +%s)  #现在日期秒数
declare -i date_total_s=$((${date_dem}-${date_now}))  #剩余秒数
declare -i date_d=$((${date_total_s}/60/60/24))  #转为天数
if [ "${date_total_s}" -lt "0" ];then #判断是否退伍,-lt表示小于，<在这里会认为重定向
   echo "you had been before:"$((-1*${date_d}))" ago"
else 
   declare -i date_h=$(($((${date_total_s}-${date_d}*60*60*24))/60/60))
   echo "you will afer ${date_d} days and ${date_h}hours"
fi       

