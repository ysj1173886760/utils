#! /user/bin/bash

# simple implementation of split string using tldr

res=$(echo $2 | tr "$1" "\n")

for addr in $res
do
	echo "$addr"
done
