import string
import operator
import sys
import csv

def maxFollowers():
    FilePath = 'C:/Users/Alex Nelson/Desktop/twitterData.txt' 
    output = []
    with open (FilePath, encoding = "latin-1") as twitterFile:
        tweets = twitterFile.readlines()
          
    
    for tweet in tweets:
        tweetInfo = tweet.split(' ')
        numberFollowers = int(tweetInfo[-2])
        info = (tweetInfo[0], numberFollowers)
        output.append(info)

        
    sortedList = sorted(output, key=lambda tup:(tup[1]), reverse=True)
    
    maxTen = (sortedList[:10])
    
    maxFollowersFile = open('C:/Users/Alex Nelson/Desktop/maxFollowers.csv', 'w')  
    with maxFollowersFile:  
        writer = csv.writer(maxFollowersFile)
        for row in maxTen:
            writer.writerow(row)

maxFollowers()
