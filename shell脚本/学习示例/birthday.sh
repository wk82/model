
#!/bin/bash
#read -p "enter birthday date,ex%Y%M%D:" date1
#检查变量是否是数字
#自己写的
#date1_check=$(echo ${date1}| grep "[0-9]\{8\}")
#if [ "${date1_check}" == "" ];then
#    echo "enter wrong number"
#    exit 1
#fi
#计算日期

#date_birth=$(date -d "${date1}" +%s)
#date_now=$(date +%s)
#if [ "$((${date_birth} - ${date_now}))" -lt "0" ];then
#    echo "you birthday had passed $((-1*$(($((${date_birth} - ${date_now}))/60/60/24)))) days."
#else
#    echo "you birthday is $(($((${date_birth} - ${date_now}))/60/60/24)) days later."
#fi


#书上范例
read -p "input your birthday MMDD:" bir
now=$(date +%m%d)
if [ "${bir}" == "${now}"  ];then
   echo "happy"
elif [ "${bir}" -gt "${now}" ];then
   year=$(date +%Y)
   total_d=$(($(($(date -d "${year}${bir}" +%s) - $(date +%s)))/60/60/24))
   echo "your birthday will be ${total_d} later"
else
   year=$(($(date +%Y)+1))
   total_d=$(($(($(date -d "${year}${bir}" +%s) - $(date +%s)))/60/60/24))
   echo "your birthday will be ${total_d} later"
fi

