import string
import operator
import sys

def maxFollowers():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = 'C:/Users/##/Desktop/' + INPUTFILE + '.txt' ##ADD USER FILE PATH

    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        twitter=myFile.readlines()

    l = {}

    for dat in twitter:
        fileTemp = dat.split()
        if fileTemp[0] not in l:
            l[fileTemp[0]] = int(fileTemp[-2])

    l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)
    outputFile = open('C:/Users/##/Desktop/maxFollowers.txt', 'w', encoding = "utf-8") ##ADD USER FILE PATH
    outputFile.write("The top 10 users who has the maximum followers: " + "\n\n")

    for i in range (0, 10):
        outputFile.write(str(i+1) + ". Username: " + l[i][0] + " -> Number of Followers: " + str(l[i][1]) + "\n\n")
    outputFile.close

maxFollowers()
