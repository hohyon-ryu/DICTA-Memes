output=meme_cluster2

hadoop fs -rmr $output

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input meme_cluster/part* -output $output \
  -file mapper2.py -mapper mapper2.py \
  -file reducer.py -reducer reducer.py \
  -numReduceTasks 16

rm -rf $output
hadoop fs -get $output $output

