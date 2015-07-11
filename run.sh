# Runs the two executables on the example data. 
~/bin/spark-1.4.0/bin/spark-submit ./src/wordcount.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
~/bin/spark-1.4.0/bin/spark-submit ./src/median.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

# To run the tests, uncomment the following lines.
# ~/bin/spark-1.4.0/bin/spark-submit ./src/test_wordcount.py 
# ~/bin/spark-1.4.0/bin/spark-submit ./src/test_median.py