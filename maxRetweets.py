import string
import operator
import sys
import csv

def maxRetweets():
    FilePath = 'C:/Users/Alex Nelson/Desktop/twitterData.txt' 
    output = []
    with open (FilePath, encoding = "latin-1") as twitterFile:
        tweets = twitterFile.readlines()
          
    
    for tweet in tweets:
        tweetInfo = tweet.split(' ')
        numberRetweets = int(tweetInfo[-1])
        info = (tweetInfo[0], numberRetweets)
        output.append(info)
        
    sortedList = sorted(output, key=lambda tup:(tup[1]), reverse = True)
    maxTen = (sortedList[:10])
    
    maxRetweetsFile = open('C:/Users/Alex Nelson/Desktop/maxRetweets.csv', 'w')  
    with maxRetweetsFile:  
        writer = csv.writer(maxRetweetsFile)
        for row in maxTen:
            writer.writerow(row)

maxRetweets()
