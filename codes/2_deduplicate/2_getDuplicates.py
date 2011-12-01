#deduplicate!
import glob
import re
import pickle
import sys
import time
import os
currenttime=time.time()

def getContent(line):
  data=line.strip()

  data=line.split("\t")

  docno=data[0]
  vecSet=set(data[1].split(","))

  return docno, vecSet

def compareDocs(vec1, vec2):
  compDic={}

  same=len(vec2 & vec1)
  
  return float(same)/min(len(vec1), len(vec2))
   

AllDocs={}

i=0

file_name=sys.argv[1]
if os.path.exists( "del_docs/"+file_name.split("/")[1]+".set"):
  print "already exist: del_docs/"+file_name.split("/")[1]+".set"
  sys.exit()



dedup_files=glob.glob("del_docs/*")
dedup_files.sort()

delset=set()
for dedup_file in dedup_files:
  #print dedup_file
  for line in open(dedup_file):
    for doc_no in line.split(","):
      delset.add(doc_no)

print "DocsToDel: %d/%d %.2f%% " % (len(delset), 16671091, (len(delset)/16671091.0*100))


#windowSize=3
for file_name in [sys.argv[1]]:
  DocsToDel=set()
  file_info=file_name.split("/")[1]
  first=file_info.split("_")[1]
  #print file_name
  #timeelapse=time.time()-currenttime
  #currenttime=time.time()
  #print file_name, docno1, len(DocsToDel), "%fs per doc" % (timeelapse)

  i=0
  for line1 in open(file_name):
    i+=1
    docno1, doc1=getContent(line1)
    if docno1 in delset or docno1 in DocsToDel:
      #print docno1, "already in list"
      continue
    #print doc1
    #timeelapse=time.time()-currenttime
    #currenttime=time.time()
    #print i, file_name, docno1, len(DocsToDel), "%fs per doc" % (timeelapse)

    if len(doc1)<5:
      DocsToDel.add(docno1)
      continue
    #print doc1
    windowSize=len(doc1)/9
    if windowSize>2:
      windowSize=2
    windowSize=1
    lowerbound=len(doc1)-windowSize
    if lowerbound<5:
      lowerbound=5
    for fileNo in range(lowerbound, len(doc1)+windowSize):
      try:
        f=open("file_vec/%05d_%s" % (fileNo, first))
        #print "processing", "file_vec/%05d_%s" % (fileNo, first)
      except:
        #print fileNo,"not exist"
        continue
      for line2 in f:
        docno2, doc2=getContent(line2)
        if docno2 in DocsToDel:
          continue
        if docno1!=docno2:
          score=compareDocs(doc1,doc2)
          if score>0.85:
            #print file_name, fileNo, score
            DocsToDel.add(docno2)
      f.close()
  

  timeelapse=time.time()-currenttime
  currenttime=time.time()
  print file_name, "%d docs to del, %.2fs for %d docs, %.2f spd" % (len(DocsToDel), timeelapse, i, (timeelapse/i))

  
  pickleFileName = "del_docs/"+file_name.split("/")[1]+".set"
  pickleFile = open(pickleFileName, 'w')
  pickleFile.write(",".join(DocsToDel))
  #pickle.dump(docno_to_del, pickleFile, pickle.HIGHEST_PROTOCOL)
  pickleFile.close()




