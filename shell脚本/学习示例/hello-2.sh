#!/bin/bash
if [ "${1}" = "hello" ];then
echo "hello"
elif [ "${1}" = "" ];then
echo "you must input parameters, ex> {${0} someword}"
else
echo "the only is "hello", ex> {${0},hello}"
fi
