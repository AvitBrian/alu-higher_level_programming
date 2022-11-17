#!/usr/bin/bash
a=3
content=("type" "id" "No" "Yes" "yes" "No" "True" "True" "True" "True" "True" "False" "True" "True")
for i in ${!content[@]};do
	echo "${content[$i]}">> $i-answer.txt
done
