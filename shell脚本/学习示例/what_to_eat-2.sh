#!/bin/bash
eat[1]="麦当当"
eat[2]="KFC"
eat[3]="A"
eat[4]="B"
eat[5]="C"
eat[6]="D"
eat[7]="E"
eat[8]="F"
eat[9]="G"
eatnum=9
eated=0
while [ "${eated}" -lt 3 ]
do
   check=$((${RANDOM}*${eatnum}/32767+1))
   mycheck=0
   if [ "${eated}" -ge 1 ];then
       for i in $(seq 1 ${eated})
       do
           if [ ${eatedcon[$i]} = ${check} ];then
                mycheck=1
           fi
       done
    fi
    if [ ${mycheck} = 0 ];then
         echo "eat ${eat[${check}]}"
         eated=$((${eated}+1))
         eatedcon[${eated}]=${check}
    fi
done     
