#!/bin/bash
read -p "please input (Y/N):" yn
[ "${yn}" = "Y" -o "${yn}" = "y" ] && echo "ok" && exit 0  #bash等号用 =，不能用==
#[ "${yn}" == "Y" -o "${yn}" == "y" ]&& echo "OK,continue"&& exit 0
[ "${yn}" = "N" -o "${yn}" = "n" ]&& echo "interrupt"&& exit 0
echo "i don't konw" && exit 0
