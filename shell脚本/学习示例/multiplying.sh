#!/bin/bash/
#数值运算
echo "you should input 2 numbers,i will multiplying them! \n"
read -p "first number: " firstnu
read -p "second number:" secondnu
total=$((${firstnu}*${secondnu}))
echo "\nthe result of ${firstnu}*${secondnu} is ${total}"
