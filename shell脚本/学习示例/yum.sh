#!/bin/bash/
#yum安装范例，判断某个包没有就安装
[ ! -d /root/bakrepo ] && mkdir -p /root/bakrepo   #判断如果没有bakrepo目录，则创建该目录
[ $? -eq 0 ] && mv /etc/yum.repos.d/CentOS-* /root/bakrepo #判断如果上面创建目录成功，则将CentOS文件转移到bakrepo目录
cat > /tmp/base.repo << EOF   #创建base.repo文件，并输入内容，EOF结束
[cdrom]
name="cdrom"
base=file:///misc/cd
gpgcheck=0
EOF
rpm -q httpd &> /dev/null || yum install httpd  #查看是否由httpd包，如没有则安装
[ $(yum list installed | grep "httpd" | wc -l）-eq 0 ] && yum install httpd  #另外一种判断方法，不够简洁
