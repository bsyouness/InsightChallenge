import sys
from operator import add
from pyspark import SparkContext


def wordcount(filename):
    if filename is None:
        print("File name is missing")
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(filename, 1)
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    sc.stop()

if __name__ == "__main__":
    filename = "../tweet_input/tweets.txt"
    wordcount(filename)
