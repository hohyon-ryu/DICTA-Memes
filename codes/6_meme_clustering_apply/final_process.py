#!/usr/bin/env python
import sys
import operator
import time

clusterCentroids=[]
#clusters=[]

def getSim(data, cent):
  try:
    return len(set(data) & cent)/ ( ( float(len( set(data) )) + len(set(cent)) ) / 2 )
  except:
    return 0

def delStopwords(wordlist=[]):
  stopwords=set(["a","about","above","after","again","against","all","also","am","an","another","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours ","ourselves","already","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", ""] )

  stopcnt=0.0
  outwordlist=[]
  for word in wordlist:
    if word.isdigit():
      outwordlist.append("numeric")
    else:
      if word not in stopwords:
        outwordlist.append(word)
    
  return outwordlist

def showTime():
  global curtime, time_elap
  time_elap=time.time()-curtime
  curtime=time.time()    
  sys.stderr.write("time elapsed:%f\n" % (time_elap))

def updateCentroid(cent, data):
  for word in data:
    cent.add(word)
  return cent  

#Read the Centroids
curtime=time.time()
line_no=0
clusterCents={}
clusterCentsList=[]
for line in open("final_cluster_centroids_indexed"):
  data=line.strip().split(",")
  data=set(data)
  data=data-set([""])
  clusterCentsList.append(data)

  for word in data:
    try:
      clusterCents[word].add(line_no)
    except:
      clusterCents[word]=set([line_no])
  
  line_no+=1

sys.stderr.write("Read Centroids: "+str(len(clusterCentsList))+"\n")

showTime()


FinalClustering={}
line_no=0


for line in sys.stdin:

  line_no+=1
  if line_no%100==0:
    sys.stderr.write(str(line_no)+" "+str(len(FinalClustering))+"\n")

  meme=line.strip()

  data=meme.replace("'", " ")
  data=data.split(" ")
  data=set(delStopwords(data))
  settled=0

  #Get the Candidates!
  candis={}
  candisOnes=set()
  for word in data:
    if word=="numeric":
      continue
    for docno in clusterCents[word]:
      
      if docno in candisOnes:
        try:
          candis[docno]+=1
        except:
          candis[docno]=2
      else:
        candisOnes.add(docno)


  sorted_candis=sorted(candis.iteritems(), key=operator.itemgetter(1),  reverse=True)
  #print sorted_candis
  candis = [x[0] for x in sorted_candis]

  #print candis
  clusterupdate_flag=False

  if len(candis)==0:
    sys.stderr.write("no candidates for: "+str(line_no)+", "+meme+"\n")
    continue

  cnt=0
  for i in candis:
    cent=clusterCentsList[i]
    #print data, cent
    #print getSim(data, cent)
    if getSim(data, cent)>0.6:
      cnt+=1
      print str(i)+"\t"+meme
      clusterupdate_flag=True
      break

  if (clusterupdate_flag==False):
    for i in candisOnes:
     if getSim(data, cent)>0.6:
      cnt+=1
      print str(i)+"\t"+meme
      clusterupdate_flag=True
      break
       
  if (clusterupdate_flag==False):
    sys.stderr.write("missed: "+str(line_no)+", "+meme+"\n")
    sys.stderr.write("%s placed into %d, %s\n" % (meme, candis[0], str(clusterCentsList[candis[0]])) )
    print str(candis[0])+"\t"+meme

