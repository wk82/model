#!/bin/bash
read -p "please input (Y/N):" yn
if [ "${yn}" = "Y" ] || [ "${yn}" = "y" ];then
echo "ok"
elif
[ "${yn}" = "N" ] || [ "${yn}" = "n" ];then
echo "interrupt"
else
echo "i dont know"
fi
