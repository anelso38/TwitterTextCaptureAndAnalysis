import string
import operator
import sys
import csv

def mostTweetsPerHour():
    FilePath = 'C:/Users/Alex Nelson/Desktop/twitterData.txt' 
    infoHours = []
    with open (FilePath, encoding = "latin-1") as twitterFile:
        tweets = twitterFile.readlines()
          
    output = []
    
    for tweet in tweets:
        tweetInfo = tweet.split(' ')
        date = tweetInfo[1].split(":")
        hour = date[-3]
        usernames = tweetInfo[0]
        output.append(usernames)
        userInfo = (usernames, hour)
        infoHours.append(userInfo)
        
    users = []
    for user in output:
        if user not in users:
            users.append(user)
                  
          
    mostTweets= []
    for u in users:
        for i in infoHours:
            if i[0] == u:
                count = infoHours.count(i)
                mostTweets.append(count)
            list = (i,count)
            mostTweets.append(list)
        
    print(mostTweets)
        
        
    sortedList = sorted(mostTweets, key=lambda tup:(tup[1]))
    maxTen = (sortedList[-10:])
    
    maxTweetsFile = open('C:/Users/Alex Nelson/Desktop/mostTweetsPerHour.csv', 'w')  
    with maxTweetsFile:  
        writer = csv.writer(maxTweetsFile)
        for row in maxTen:
            writer.writerow(row)

mostTweetsPerHour()
