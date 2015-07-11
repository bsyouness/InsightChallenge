# Insight Data Engineering - Coding Challenge

## Introduction

This repository contains tools to analyze tweets per the Insight Coding Challenge requirements. The tweets are simulated by a text file. I decided to use Spark for this project in order to make it easily scalable. The features are currently fairly primitive, but could be easily improved.

You can run the code using Travis, by following this link:

[![Build Status](https://travis-ci.org/bsyouness/InsightChallenge.svg?branch=master)](https://travis-ci.org/bsyouness/InsightChallenge)

## Challenge Summary

The src folder contains two executables:

### Wordcount

The first (wordcount.py) calculates the total number of times each word in the input file has been tweeted. It uses a SparkContext collection to load the input file that contains the tweets. It then uses a map-reduce to:
Tokenize the tweets into words and initialize counts for each word, 
Reduce sums the counts, producing a histogram.

wordcount.py runs in linear time.

### Median

The second one (median.py) calculates the median number of *unique* words per tweet, and updates this median as tweets come in. The median calculation is performed using heaps. The number of words in tweets that were previously processed are stored in two heaps. The algorithm complies with two invariants. The first invariant is that all the elements in one heap are smaller or equal to the ones in the other heap. We call the heap with the smallest element leftheap, and the heap with the largest ones rightheap. The second invariant is that at any given time, the length of the heaps differ by at most one. Whenever a new tweet comes in, it is inserted in rightheap or leftheap to maintain the first invariant. Then the heaps are re-balanced if needed: their lengths are adjusted to maintain the second invariant. This algorithm is based on the discussion which appears at:
http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers



In terms of running time, each insertion and deletion is performed in constant time. The overall complexity is linear as well. 

