#!/bin/bash

i=1
result=""
while [ $i -le 3 ]
do
	result="$result $USER"
	((i++))
done
echo $result

