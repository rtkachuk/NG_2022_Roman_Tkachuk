userInput = input("Enter string: ")
letterCounts = {}
uniqueSymbols = set(userInput)
for unique in uniqueSymbols:
    letterCounts[unique] = userInput.count(unique)
print (letterCounts)