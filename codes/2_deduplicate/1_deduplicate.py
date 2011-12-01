#deduplicate!
import glob
import re
import pickle
import sys

dedup_folder="../../data/1_cleaned/"+sys.argv[1]+"/*"

dedup_files=glob.glob(dedup_folder)
dedup_files.sort()
from operator import itemgetter, attrgetter

def getContent(line):
  data=line.strip()

  reg=re.search('<DOCNO>(.*?)</DOCNO>', data)
  docno=reg.group(1)

  reg=re.search('<DOC>(.*?)</DOC>', data)
  doc=reg.group(1)
  text=re.sub('<[^<]+?>', ' ', doc)

  vec=re.findall("\w+", text)

  vecDic=set()
  first=""
  if (len(vec)>0):
    first=vec[0][:1].lower()
  for word in vec:
    word=word[:4].lower()
    vecDic.add(word)
    #try:
    #  vecDic[word]+=1
    #except:
    #  vecDic[word]=1

  return docno, vecDic, first

def compareDocs(vec1, vec2):
  compDic={}

  same=len(vec2 & vec1)
  
  return float(same)/max(len(vec1), len(vec2))
   

AllDocs={}

#print "Loading all the docs (first 1000 chars) to Memory. Crazy, huh?"

print sys.argv[1]
for dedup_file in dedup_files: 
  #sys.stderr.write(dedup_file+"\n")
  for line in open(dedup_file):
    docno, doc, first=getContent(line)

    open("file_vec/%05d_%s" % (len(doc), first),'a').write( str(docno)+"\t"+",".join(doc)+"\n" )


