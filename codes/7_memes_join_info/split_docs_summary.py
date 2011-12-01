import sys
import math
i=0
prevCate=-1
doclist=[]
doccnt=set()
srccnt=set()
wordcntS=set()
datesS=set()
wordcnt=0

for line in sys.stdin:
  data=line.strip().split("\t")

  cate=data[0]
  meme=data[1]
  docsrcs=data[2].split(",")
  docs=[doc.split("|")[0] for doc in docsrcs]
  srcs=[doc.split("|")[1] for doc in docsrcs]

  dates=[doc[7:15] for doc in docs]
  #print dates

  srcs=set(srcs)

  if prevCate!=cate and prevCate!=-1:
    print "%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%s" % (prevCate, math.log(1.0+len(doclist)), math.log(1.0+float(wordcnt)/len(doclist)), math.log(1.0+len(doccnt)/float(len(doclist))), math.log(1.0+len(srccnt)/float(len(doclist))), len(wordcntS)/float(wordcnt), math.log(1.0+len(datesS)), float(len(doccnt))/len(datesS), ",".join(doclist) )
    doclist=[]
    doccnt=set()
    srccnt=set()
    wordcntS=set()
    datesS=set()	
    wordcnt=0
  
  memewords=meme.strip().split(" ")
  wordcnt+=len(memewords)

  doclist.append( str( (meme, len(docs), len(srcs)) ) )
  doccnt|= set(docs) 
  srccnt|=srcs 
  wordcntS|=set(memewords)
  datesS|=set(dates)

  prevCate=cate
  #print "%s\t%s\t%d\t%d" % (cate, meme, len(docs), len(srcs))


