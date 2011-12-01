#deduplicate!
import glob
import re
import pickle
import os

dedup_folder="../2_deduplicated/20080115/*"

dedup_files=glob.glob("del_docs/*")
dedup_files.sort()

delset=set()
for dedup_file in dedup_files:
  print dedup_file
  for line in open(dedup_file):
    for doc_no in line.split(","):
      delset.add(doc_no)
  print len(delset)

cleaned_files=glob.glob("../../data/1_cleaned/*/*")
cleaned_files.sort()

for cleaned_file in cleaned_files:

  dedu_file=cleaned_file.replace("1_cleaned", "2_deduplicated")
  #print cleaned_file, "to", dedu_file

  #f=open(dedu_file+"_temp", "w")
  f=open(dedu_file, "w")
  cnt=0
  for line in open(cleaned_file):
    reg=re.search('<DOCNO>(.*?)</DOCNO>', line)
    docno=reg.group(1)
    if docno in delset:    
      cnt+=1
      continue
    f.write(line)
  f.close()

  print dedu_file, cnt, "duplicates deleted"
  #os.system("mv "+dedu_file+"_temp "+dedu_file)

    



