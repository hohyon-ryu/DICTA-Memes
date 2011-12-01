output=blog_memes_2

hadoop fs -rmr $output

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input blog_memes_1/part* -output $output \
  -file mapper2.py -mapper mapper2.py \
  -file reducer2.py -reducer reducer2.py \
  -numReduceTasks 264

rm -rf $output
hadoop fs -get $output $output

