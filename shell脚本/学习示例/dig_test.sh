#!/bin/bash
#创建文件
#read -p "input filename:" filename
#判断文件是否为空或是否重复

for a in {1..20}
do
    dig magicm.cmcm.com | grep Query* >> dig.txt 2>/dev/null
done
