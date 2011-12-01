#!/usr/bin/env python
#Reducer

import sys
import operator
import re


def printOutput(prev_phrase, output):
	print prev_phrase+"\t"+",".join(output)

prev_phrase=""
output=[]
cnt=0

skip_flag=False
for line in sys.stdin:
	data=line.strip().split("\t")
	phrase=data[0]
	if prev_phrase!=phrase and len(output)>0:
		printOutput(prev_phrase,output)
		output=[]
		cnt=0
		
	if skip_flag==False:
		output.append(data[1])

	prev_phrase=phrase
	cnt+=1

printOutput(prev_phrase,output)
