""" Functions for processing tweets
    This is nearly identical to code in the PySpark example library:
    https://spark.apache.org/examples.html
"""

import sys
from operator import add
from pyspark import SparkContext

def wordcount(input_path, output_path):
    """ Computes a histogram of word occurences from a set of tweets.

    Args: 
        input_path: the name of the file to read, 
        output_path: the name of the file to output to.
    """

    # Initiate a SparkContext instance.
    sc = SparkContext(appName="PythonWordCount")
    
    # Load the input file as a Spark collection.
    lines = sc.textFile(input_path, 1)

    # This is a map-reduce.
    # The map tokenizes the tweets into words and initializes counts for each word.
    # The reduce sums the counts, producing a histogram.
    # The histogram in the Insight example was sorted alphabetically, so we're doing a sort here.
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add) \
                  .sortByKey()
    
    # Convert the output to a Python list.
    output = counts.collect()

    # Write the list of words and their count to an output file
    with open(output_path, "w+") as f:
        for (word, count) in output:
            f.write("{:<50}{:10}\n".format(word, str(count)))

    # Kill the SparkContext instance.
    sc.stop()

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if (input_path is None) | (output_path is None):
        print("Usage is: wordcount.py <input_path> <output_path>")
        exit(-1)

    wordcount(input_path, output_path)
