#!/usr/bin/env python


from BeautifulSoup import BeautifulSoup
#import nltk
#nltk.download()

#ssh hr@stingray.ischool.utexas.edu 'time zcat /media/8bbede80-029c-4334-ba70-d069e4fb5904/Blogs08Collection/200802*/permalinks-*' | python clean_blogs08.py > ../cleaned_200802.data

#import chunker
#from nltk.corpus import stopwords
import sys
import re
import time
currenttime=time.time()
sys.stderr.write("Mapper Started\n")


timeelapse_decruft=0
timeelapse_lg=0

#export HUNPOS=/home/disk1/Hohyon/20110825_Blog_Cleanup/decruft/hunpos/hunpos-tag

#hunpos = nltk.tag.HunposTagger("en_wsj.model") 
def my_split(s, seps):
  res = [s]
  for sep in seps:
    s, res = res, []
    for seq in s:
      res += seq.split(sep)
  return res

def process_buffer(data):
  global lg_dist
  #global timeelapse_decruft
  #global timeelapse_lg
  
  global hunpos

  data=data.strip()

  #print data

  reg=re.search('<DOCNO>(.*?)</DOCNO>', data)
  docno=reg.group(1)

  reg=re.search('<PERMALINK>(.*?)</PERMALINK>', data)
  perma=reg.group(1)

  reg=re.search('\/\/(.*?)\/', perma)
  source=reg.group(1)

  reg=re.search('<DOC>(.*?)</DOC>', data)
  doc=reg.group(1)

  final_text=' '.join(BeautifulSoup(doc).findAll(text=True))  
  final_text=str(final_text).lower()

  #sentences=my_split(final_text, [".","?","!","  ", ",", "\n", "(", ")", "--"])
 

  print docno+"\t"+source+"\t"+final_text



data_processed=0

prev_len=0
for line in sys.stdin:
  if line.startswith("<DOCNO>"):
    if len(line)>10:
      try:
        process_buffer (line)
      except:
        sys.stderr.write("Error Processing a line")
        continue

      data_processed+=1
      timeelapse=time.time()-currenttime

      if data_processed%1000==0:
        reg=re.search('<DOCNO>(.*?)</DOCNO>', line)
        docno=reg.group(0)
        sys.stderr.write ("\nProcessed Documents: "+str(data_processed)+"\n")
        sys.stderr.write ("Last Document: "+docno+"\n")
        sys.stderr.write ("Elapsed Time: "+str(time.strftime("%H:%M:%S", time.gmtime(timeelapse)))+"\n")
        sys.stderr.write ("Average Time per Document: "+str(timeelapse/data_processed)+"\n")

        prev_len=0

sys.stderr.write("Mapper Finished\n")
