#!/bin/bash
while [ "${yn}" != "yes" -a "${yn}" != "YES" ]
do 
     read -p "please input yes/YES to stop this program:" yn
done
echo "ok"
