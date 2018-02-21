def mostTweetsPerTimeline():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = 'C:/Users/##/Desktop/' + INPUTFILE + '.txt' ##ADD USER FILE PATH

    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        twitter=myFile.readlines()
    l = {}
    for dat in twitter:
       
        fileTemp = dat.split()
        if fileTemp[0] in l:
            l[fileTemp[0]] +=1
        else:
            l[fileTemp[0]] = 1
    l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)
 
    outputFile = open('C:/Users/##/Desktop/mostTweetsPerTimeline.txt', 'w', encoding = "utf-8") ##ADD USER FILE PATH
    outputFile.write("The top 10 users who have tweeted the most for the entire timeline: \n")
    for i in range (0,10):
        outputFile.write("The user " + l[i][0] + " tweeted " + str(l[i][1]) + " times" + "\n")
        
    outputFile.close
mostTweetsPerTimeline()
