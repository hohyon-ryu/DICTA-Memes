#!/usr/bin/env python
   
import thread
import datetime
import glob
import time
import os
import sys

currenttime=time.time()

folders=glob.glob("../../data/3_compressed/concat/*")


def runFolders(folders, thread_no):
  print thread_no, len(folders)
  for folder in folders:
    print folder
    #pass
    foldername=folder.split("/")
    foldername=foldername[-1]
    os.system("nice -n20 cat %s | python mapper.py > ../../data/3_compressed/concat_strip/%s.strip " % (folder, foldername) ) 
  print thread_no, "Done!!"

folders.sort()

num_of_process=6

folder_dic={}
i=1
for folder in folders:
  try:
    folder_dic[i%num_of_process].append(folder)
  except:
    folder_dic[i%num_of_process]=[folder]
  i+=1

for j in range(num_of_process):
  #print folder_dic[j], j
  thread.start_new_thread(runFolders,( folder_dic[j], j ) )
  time.sleep(1)

while 1:
  if (raw_input('enter kill to kill the process or just enter to see the time elapsed:')=="kill"):
    sys.exit()
  else:
    timeelapse=time.time()-currenttime
    print "Time: "+str(time.strftime("%d %H:%M:%S", time.gmtime(timeelapse)))

