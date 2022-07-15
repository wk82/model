#!/bin/base
function printit() {
     echo -n "your choice is "
}
echo "this program will print your selection !"
case ${1} in
     "one")
      printit;echo ${1} | tr 'a-z' 'A-Z'
      ;;
      "{two|TWO}")
      printit;echo ${1} | tr 'a-z' 'A-Z'
      ;;
      *)
      echo "usage ${0} {one|two}"
      ;;
esac
