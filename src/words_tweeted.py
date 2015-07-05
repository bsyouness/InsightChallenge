# example of program that calculates the total number of times each word has been tweeted.
import re

tweetinfile = open("../tweet_input/tweets.txt")
tweets = tweetinfile.read()

tweetwords = []
tweetwords = re.split(" |\n|\t", tweets)
tweetset = set(tweetwords)
tweetset = sorted(tweetset)
tweetcount = []
tweetoutfile = open("../tweet_output/ft1youness.txt", "w+")

for word in tweetset:
    counter = 0
    for tweetword in tweetwords:
        if word == tweetword:
            counter += 1
    tweetcount.append((word, counter))
    tweetoutfile.write("{:<50}{:10}\n".format(word, str(counter)))

#for x in tweets:






