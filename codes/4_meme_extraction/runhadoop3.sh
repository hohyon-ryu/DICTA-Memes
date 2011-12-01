output=blog_memes_3

hadoop fs -rmr $output

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input blog_memes_2/part* -output $output \
  -file mapper3.py -mapper mapper3.py \
  -file reducer3.py -reducer reducer3.py \
  -numReduceTasks 264

rm -rf $output
hadoop fs -get $output $output

