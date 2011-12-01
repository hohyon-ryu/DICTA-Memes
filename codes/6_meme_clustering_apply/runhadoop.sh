output=meme_cluster

hadoop fs -rmr $output

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input memes_v1.2.list.split/* -output $output \
  -file mapper.py -mapper mapper.py \
  -file reducer.py -reducer reducer.py \
  -file final_cluster_centroids_indexed \
  -numReduceTasks 40

rm -rf $output
hadoop fs -get $output $output

