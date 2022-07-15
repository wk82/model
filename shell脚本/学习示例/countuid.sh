#!/bin/bash
#
#**************************************************************
#Author:    wk
#Date:      2020-08-20
#FileName:  countuid.sh
#Copyright: 2020 All right reserved
#**************************************************************
#对第10行、第20行uid值相加
#取第10行uid
num10=$(sed -n '10p' /etc/passwd | cut -d ':' -f 3)
num20=$(sed -n '20p' /etc/passwd | cut -d ':' -f 3)
sum=$((${num10} + ${num20}))
echo "sum is ${sum}"
exit 0
