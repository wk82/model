#!/bin/bash
#互动方式
echo "this program will print your selection !"
read -p "input your choice:" choice
case ${choice} in
        "one")
        echo "your choice is one"
        ;;
        "two")
        echo "your choice is two"
        ;;
        "three")
        echo "your choice is three"
        ;;
        *)
        echo "no choice"
        ;;
esac
