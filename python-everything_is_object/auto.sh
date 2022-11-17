#!/usr/bin/bash
a=20
content=("Yes" "Yes" "No" "Yes" "True" "False" "True" "No" "Yes")
for i in ${!content[@]};do
	sum=$((a+i))
	echo "${content[$i]}">> "$sum-answer.txt"
done
