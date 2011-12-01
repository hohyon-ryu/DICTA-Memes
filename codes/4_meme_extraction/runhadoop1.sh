output=blog_memes_1

hadoop fs -rmr $output

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input htmlstrip/* -output $output \
  -file mapper1.py -mapper mapper1.py \
  -file reducer1.py -reducer reducer1.py \
  -numReduceTasks 264

rm -rf $output
hadoop fs -get $output $output

