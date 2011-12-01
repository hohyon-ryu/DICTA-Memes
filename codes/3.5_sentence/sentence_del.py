import nltk
import sys

for line in open(sys.argv[1]):
	data=line.split("\t")
	#print data
	docid=data[0]
	source=data[1]
	text=" ".join(data[2:]).strip()
	#print docid, source, text
	tokenizer = nltk.PunktSentenceTokenizer()
	text=tokenizer.tokenize(text)
	output=docid+"\t"+source+"\t"+str(text)+"\n"
	
	open("splitted/%s" % (sys.argv[1].split("/")[-1]), "a").write( output )

