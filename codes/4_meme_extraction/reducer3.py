#!/usr/bin/env python

#Reducer 2

import sys
import operator
import re

prev_phrase=""
output=[]
for line in sys.stdin:
	data=line.strip().split("\t")
	phrase=data[0]

	if prev_phrase!=phrase and len(output)>0:
		if len(output)>5:
			if len(prev_phrase)<200:
				print prev_phrase+"\t"+"|".join(output)

		output=[]
		
	output.append(data[1])

	prev_phrase=phrase

if len(output)>5:
	if len(prev_phrase)<200:
		print prev_phrase+"\t"+"|".join(output)
