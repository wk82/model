#!/bin/bash
#输入文件名并判断是否有输入字符串
read -p "input a filename :" filename
test -z ${filename} && echo "the filename ${filename} do not exist" && exit 0
#判断文件是否存在，若不存在显示信息并结束脚本
test ! -e ${filename} && echo "the filename ${filename} do not exist" && exit 0
#判断文件类型与属性
test -f ${filename} && filetype="regulare file"
test -d ${filename} && filetype="directory"
test -r ${filename} && perm="readable"
test -w ${filename} && perm="${perm} writable"
test -x ${filename} && perm="${perm} executable"
#输出信息
echo "the filename: ${filename} is a ${filetype}"
echo "and the permissions for you are : ${perm}"
	

