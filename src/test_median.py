""" This file contains a test of spark_median, in which its output
is checked against a golden output file.
"""

import unittest
from median import spark_median

class TestSparkMedian(unittest.TestCase):

    def test_spark_median(self):
        """ Test median on provided test data.
        """

        # Define the file paths.
        input_path = "./tweet_input/tweets.txt"
        output_path = "./tweet_output/ft2.txt"
        golden_path = "./tweet_output/median_golden.txt"

        print "Running spark_median on input %s and writing output to %s" % (input_path, output_path)
        spark_median(input_path, output_path)

        # Read the contents of the output and golden files.
        with open(golden_path, "r") as f: golden=f.read()
        with open(output_path, "r") as f: out=f.read()

        # Check that the output and golden files are identical.
        self.assertEqual(golden, out)

    def test_spark_median_more(self):
        """ Test median on larger set of data.
        """
        
        # Define the file paths.
        input_path = "./tweet_input/more_tweets.txt"
        output_path = "./tweet_output/more_ft2.txt"
        golden_path = "./tweet_output/more_median_golden.txt"

        print "Running spark_median on input %s and writing output to %s" % (input_path, output_path)
        spark_median(input_path, output_path)

        # Read the contents of the output and golden files.
        with open(golden_path, "r") as f: golden=f.read()
        with open(output_path, "r") as f: out=f.read()

        # Check that the output and golden files are identical.
        self.assertEqual(golden, out)

if __name__ == "__main__":
    unittest.main()