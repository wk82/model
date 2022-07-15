#!/bin/bash
#写下收集到的店家
eat[1]="麦当当"
eat[2]="KFC"
eat[3]="彩虹"
eat[4]="A"
eat[5]="B"
eat[6]="C"
eat[7]="D"
eat[8]="E"
eat[9]="F"
eatnum=9          #输入有几个可用的餐厅数

check=$((${RANDOM}*${eatnum}/32767+1))
echo "eat $eat{[${check}]}"




























