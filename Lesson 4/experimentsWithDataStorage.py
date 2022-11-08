import platform

dataFile = open("OSDetails.txt", "r")
fileContents = dataFile.readlines()
for line in fileContents:
    print (line, end="")
dataFile.close()