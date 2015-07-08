#!/usr/bin/env bash

# example of the run script for running the word count

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
~/bin/spark-1.4.0/bin/spark-submit ./src/wordcount.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
~/bin/spark-1.4.0/bin/spark-submit ./src/test_wordcount.py 
#spark-submit ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt