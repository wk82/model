#!/bin/bash/
echo "I will use 'touch' command to create 3 files."
read -p "Please input you filename: " fileuser
filename=${fileuser:-"filename"}            #判断有否配置文件名
#利用date指令取得需要的文件名
date1=$(date --date='2 days ago' +%Y%m%d)    #前两天的日期    
date2=$(date --date='1 days ago' +%Y%m%d)    #前一天的日期
date3=$(date +%Y%m%d)                       #今天的日期
#配置文件名
file1=${filename}${date1}                   
file2=${filename}${date2}
file3=${filename}${date3}
#创建文件
touch "${file1}"
touch "${file2}"
touch "${file3}"
