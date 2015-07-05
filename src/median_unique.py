import re
import numpy

tweetinfile = open("../tweet_input/tweets.txt")
tweets = tweetinfile.readlines()

def median(lst):
    return numpy.median(numpy.array(lst))

tweetmedian = []
#how to iterate all but first?
#tweetcount1 = None
tweetcount = []
tweetoutfile = open("../tweet_output/ft2youness.txt", "w+")

for tweet in tweets:
    tweetcount2 = len(set(tweet.split()))
    tweetcount.append(tweetcount2)
    tweetmedian.append(median(tweetcount))
    tweetoutfile.write(str(median(tweetcount)) + "\n")
    # if not tweetcount1 is None:
    #     print(tweetmedian + [tweetcount2])
    #     tweetmedian + [tweetcount2]))
    # else:
    #     tweetmedian.append(tweetcount2)
    # tweetcount1 = tweetcount2





