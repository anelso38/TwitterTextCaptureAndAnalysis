import string
import operator
import sys

def maxRetweets():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = 'C:/Users/##/Desktop/' + INPUTFILE + '.txt' ##ADD USER FILE PATH
    
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        twitter=myFile.readlines()

    l = {}

    for dat in twitter:
        fileTemp = dat.split()
        y = len(fileTemp)-2
        tweet = "\""
        for x in range (4, y):
            tweet += fileTemp[x] + " "
        tweet += " ::::;:::: " + fileTemp[0]

        if tweet not in l:
            l[tweet] = int(fileTemp[-1])

    outputFile = open('C:/Users/##/Desktop/maxRetweets.txt', 'w', encoding = "utf-8") ##ADD USER FILE PATH
    l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)
    outputFile.write("The top 10 tweets that has the max no of retweets : " +"\n\n")

    for x in range (0, 10):
        outputFile.write(str(x+1) + ". Username: " + l[x][0].split()[-1] + "\n Tweet: " + 
                         l[x][0].split("::::;::::")[0] + "\n No of retweets: " + str(l[x][1]) + "\n\n")
    outputFile.close
    
maxRetweets()
