""" This file contains a test of wordcount, in which its output
is checked against a golden output file.
"""

import unittest
from pyspark import SparkContext

from wordcount import wordcount

class TestWordCount(unittest.TestCase):

    def test_wordcount(self):
        # Define the file paths.
        input_path = "./tweet_input/tweets.txt"
        output_path = "./tweet_output/ft1.txt"
        golden_path = "./tweet_output/wordcount_golden.txt"

        print "Running wordcount on input %s and writing output to %s" % (input_path, output_path)
        wordcount(input_path, output_path)
        
        # Read the contents of the output and golden files.
        with open(golden_path, "r") as f: golden=f.read()
        with open(output_path, "r") as f: out=f.read()

        # Check that the output and golden files are identical.
        self.assertEqual(golden, out)

if __name__ == "__main__":
    unittest.main()
