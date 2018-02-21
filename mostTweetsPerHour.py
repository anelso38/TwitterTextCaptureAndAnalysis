import string
import operator
import sys

def mostTweetsPerHour():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = 'C:/Users/##/Desktop/' + INPUTFILE + '.txt' ##ADD USER FILE PATH

    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()

    l = {}
    
    for dat in data:
        fileTemp = dat.split()
        fileTemp2 = fileTemp[1].split(":")
        twitterTemp = fileTemp[0] + " " + fileTemp2[1]
        if twitterTemp in l:
            l[twitterTemp]+=1
        else:
            l[twitterTemp]=1
    l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)

    l2={}

    totalNumPostsInFile = 0
    for dat in l:
        totalNumPostsInFile+=1
        
        if(dat[0].split()[1]) in l2:
            l2[dat[0].split()[1]]+=1
        else:
            l2[dat[0].split()[1]]=1

    l2 = sorted(l2.items(), key = operator.itemgetter(1))
    totalEntriesToPrint = 10*len(l2)
    outputFile = open('C:/Users/##/Desktop/mostTweetsPerHour.txt', 'w', encoding = "utf-8") ##ADD USER FILE PATH

    for x in range (0,len(l2)):
        mSearch = 10
        
        for dat in l:
            
            if mSearch == 0:
                break
            if dat[0].split()[1] == l2[x][0]:
                outputFile.write("Username: " + dat[0].split()[0] + "\n Hour: " + l2[x][0] +"\n")
                mSearch-=1
    outputFile.close
    
mostTweetsPerHour()
