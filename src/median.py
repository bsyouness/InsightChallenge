""" Library and executable for computing a running median using Spark.
"""

import sys

from pyspark import SparkContext

from running_median import running_median

def spark_median(input_path, output_path):
    """Computes the running median of unique word counts in an input file simulating a tweet stream.

    The computation is broken into two parts. The first is a parallel map which pre-processes the 
    tweets. The second is a serial, streaming, running median.

    Args:
      input_path: The path containing the tweets, with one tweet per line.
      output_path: The path where the running median should be written.
    """

    # Initialize a SparkContext instance.
    sc = SparkContext(appName="PySparkRunningMedian")

    # Read the tweets into a Spark collection.
    lines = sc.textFile(input_path, 1)
    # We preprocess the tweets in parallel using a map.
    # The result is a collection of `int`s, counting the number of unique words in each tweet.
    unique_wordcounts = lines.map(lambda x: len(set(x.split(' '))))

    # The actual median computation appears to be inescabably serial, so we compute a running median locally,
    # using the iterator `unique_wordcounts.toLocalIterator()` to make things faster and limit memory usage.
    # NOTE: This merely streams the data through the local process; the data is not all loaded simultaneously.
    # NOTE: We are assuming the ordering of the tweets has been preserved throughout the Spark computation,
    # which is the case in the tests I ran. If this is not the case in general, we could augment the collections
    # with line numbers as keys, and use a `sortByKey` to recover the original order.
    with open(output_path, "w") as f:
        print "Writing to: " + output_path
        for m in running_median(unique_wordcounts.toLocalIterator()):
            # The FAQ asks us to truncate the result to 2 digits after the decimal. 
            # I know of no cleaner way to do this. 
            median = str("{0:.15f}".format(m))
            median = median[:median.find(".")+3]
            f.write(median + "\n")

    sc.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: median.py <input_path> <output_path>")
        exit(-1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    spark_median(input_path, output_path)