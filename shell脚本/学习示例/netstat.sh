#!/bin/bash
#告知动作
echo "now,i will detect your linux server's services"
echo "the www,ftp,ssh,and mail will be detect! \n"
#开始进行测试工作，并输出一些信息
testfile=/dev/shm/nestat_checking.txt
netstat -tuln > ${testfile}  #转存数据到内存中
testing=$(grep ":80" ${testfile})  #检查port 80 在否
if [ "${testing}" != "" ];then
echo "www is running in your system "
fi
testing=$(grep ":22" ${testfile})
if [ "${testing}" != "" ];then
echo "ftp is running"
fi
