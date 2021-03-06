[![Build Status](https://travis-ci.org/bsyouness/InsightChallenge.svg?branch=master)](https://travis-ci.org/bsyouness/InsightChallenge)

# Insight Data Engineering - Coding Challenge

## Introduction

This repository uses PySpark to analyze tweets per the [Insight Coding Challenge](https://github.com/InsightDataScience/cc-example). 

## Running the code

To install the dependencies, execute the following commands or follow the `.travis.yml` file (this has been tested on Ubuntu 14.04 x64):

    wget http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0-bin-hadoop2.6.tgz
    tar -xzf spark-1.4.0-bin-hadoop2.6.tgz
    mkdir ~/bin
    mv spark-1.4.0-bin-hadoop2.6 ~/bin/spark-1.4.0

To run the tests, run `./run_test.sh`.

To run the executables on the example data, run `./run.sh`.

## Challenge Summary

The `src` folder contains two executables for the word count and running median tasks.
They are described below.

### Wordcount

`wordcount.py` calculates the total number of times each word in the input file appears. 
This can be solved with a map followed by a reduce; see the script for more details.

`wordcount.py` takes a number of computational steps which is linear in the number of tweets, but can run in *O(log n)* sequential time steps (not computational steps) given enough parallelism. Here, the map would be executed simultaneously (in parallel). The reduce would take *O(log n)* sequential steps.

### Median

`median.py` calculates the median number of unique words per tweet, and updates this median as tweets come in (a running median). 

I wasn’t able to completely parallelize the median computation, but I did break the task in half and parallelize the first half.
First, I do a parallel map across all the tweets to calculate the number of unique words per tweet.
Second, I stream the tweets through a local process and compute a running median using [this algorithm](http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers) I found on Stack Overflow.
See `median.py` for more details.

`median.py` has complexity *O(n log n)* in the number of tweets, since the streaming median algorithm I use can do a constant number of *O(log n)* heap inserts at each step.
Unfortunately, the parallel map I do for preprocessing doesn’t improve the asymptotic scalability of the algorithm, because either way I have to do an *O(n log n)* streaming computation through a single node.
This map is only useful if the time to compute a unique word count is very high relative to the time required to take a step in the running median algorithm.

This solution does not scale as well as my first.

#### Thanks for reviewing my code :)
