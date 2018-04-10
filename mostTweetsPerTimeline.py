import string
import operator
import sys
import csv

def mostTweetsPerTimeline():
    FilePath = 'C:/Users/Alex Nelson/Desktop/twitterData.txt' 
    output = []
    with open (FilePath, encoding = "latin-1") as twitterFile:
        tweets = twitterFile.readlines()
          
    
    for tweet in tweets:
        tweetInfo = tweet.split(' ')
        usernames = tweetInfo[0]
        output.append(usernames)
        
    
    users = []
    for user in output:
        if user not in users:
            users.append(user)
            
    mostTweets = []
    for i in users:
        count = output.count(i)
        list = (i,count)
        mostTweets.append(list)
        
        
    sortedList = sorted(mostTweets, key=lambda tup:(tup[1]), reverse = True)
    maxTen = (sortedList[:10])
    
    maxTweetsFile = open('C:/Users/Alex Nelson/Desktop/mostTweetsPerTimeline.csv', 'w')  
    with maxTweetsFile:  
        writer = csv.writer(maxTweetsFile)
        for row in maxTen:
            writer.writerow(row)

mostTweetsPerTimeline()
