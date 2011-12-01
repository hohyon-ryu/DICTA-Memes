#!/usr/bin/env python

#Extender

import sys
import operator
import re

prev_phrase=""
output=[]

def checkStopwords(wordlist=[]):
	stopwords=set(["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours "," ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"] )

	stopcnt=0.0
	for word in wordlist:
		if word in stopwords:
			stopcnt+=1
		elif word.isdigit():
			stopcnt+=1

	return stopcnt/len(wordlist)

def cutPrepositions(wordlist=[]):
	preps=set(["aboard", "about", "above", "across", "after", "against", "along", "amid", "among", "anti", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "concerning", "considering", "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in", "inside", "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus", "regarding", "round", "save", "since", "than", "through", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up", "upon", "versus", "via", "with", "within", "without","and","but","is","will","can","has","have","would","may", "might"])
	#print wordlist
	if len(wordlist)==0:
                return wordlist
	if wordlist[0] in preps:
		wordlist=wordlist[1:]
	#print wordlist
	if len(wordlist)==0:
		return wordlist
	if wordlist[-1] in preps:
		wordlist=wordlist[:-1]
	#print wordlist
	return wordlist

for line in sys.stdin:
	data=line.strip().split("\t")
	current_title=data[0]
	#print "-----",current_title

	memes=data[1].split("/")

	meme_index_dic={}	
	index_list=[]
	for meme in memes:
		meme_split=meme.split("=")

		meme_trigram=meme_split[0]
		meme_index=meme_split[1]

		title,index =meme_index.split(",")
		if title==current_title:
			index_list.append(int(index))
			tri=meme_trigram.split(" ")
			meme_index_dic[int(index)]=tri

	index_list.sort()
	cnt=0
	current_output=[]
	for i in index_list:

		if cnt>0:
			#print index_list[cnt-1]
			if i-index_list[cnt-1]<=3:
				current_output.extend(meme_index_dic[i][3-(i-index_list[cnt-1]):])

			else:
				current_output=cutPrepositions(current_output)
				if len(current_output)>0:
					if (checkStopwords(current_output)<0.65):
						print " ".join(current_output)+"\t"+current_title
				#current_output=[]
				current_output=meme_index_dic[index_list[cnt]]

		cnt+=1
	current_output=cutPrepositions(current_output)
	if len(current_output)>0:
		if (checkStopwords(current_output)<0.65):
			print " ".join(current_output)+"\t"+current_title

				
