import sys

cluster_dic={}
for line in open("../../data/5_clustered_memes/memes_cluster.table"):
  data=line.strip().split("\t")
  for meme in data[1].split(","):
    cluster_dic[meme]=data[0]

#print cluster_dic
sys.stderr.write("Cluster Done\n")

source_dic={}
for line in open("../../data/5_clustered_memes/doc-source.table"):
  data=line.strip().split("\t")
  source_dic[data[0]]=data[1]

sys.stderr.write("Source Done\n")

i=0
for line in sys.stdin:
  data=line.strip().split("\t")
  meme=data[0]
  docs=data[1].split("|")
  docs.sort()

  i+=1
  if i%10000==0:
    sys.stderr.write("%d\n" % (i))

  j=0
  for doc in docs:
    docs[j]=doc+"|"+source_dic[doc]
    j+=1

  try:
    print cluster_dic[meme]+"\t"+meme+"\t"+",".join(docs)
  except:
    sys.stderr.write("%d. %s not found\n" % (i, meme))


