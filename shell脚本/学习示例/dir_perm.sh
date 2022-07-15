#!/bin/bash
#先检查文件是否存在
read -p "please input a dir:" dir
if [ "${dir}" = "" -o ! -d "${dir}" ];then
   echo "this ${dir} is not exist"
   exit 1
fi
#文件测试
filelist=$(ls ${dir})
for filename in ${filelist}
do 
   perm=""
   test -r "${dir}/${filename}" && perm="${perm} readable"
   test -w "${dir}/${filename}" && perm="${perm} writable"
   test -x "${dir}/${filename}" && perm="${perm} executable"
   echo "the first ${dir}/${filename}'s permission is ${perm}"
done
