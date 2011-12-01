import sys
import random

i=0
prevCate=-1
doclist=[]


sampled=set(random.sample(xrange(2019727), 1500))


for line in sys.stdin:
  data=line.strip().split("\t")

  cate=data[0]
  meme=data[1]
  docsrcs=data[2].split(",")
  docs=[doc.split("|")[0] for doc in docsrcs]
  #srcs=[doc.split("|")[1] for doc in docsrcs]


  if prevCate!=cate and prevCate!=-1:
    if int(prevCate) in sampled:
      print "%s\t%d%s" % (prevCate, ",".join(doclist) )
    doclist=[]

  doclist.append( meme )

  prevCate=cate
  #print "%s\t%s\t%d\t%d" % (cate, meme, len(docs), len(srcs))


