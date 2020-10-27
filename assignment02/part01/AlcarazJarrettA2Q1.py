""" AlcarazJarrettA2Q1

COMP 1012 SECTION A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 2, Question 1
AUTHOR: Charleson J. Alcaraz
VERSION: 2020-Oct-23

PURPOSE: Print the 10 most and least frequently drawn numbers
         from a CSV file of winning Powerball Numbers.
"""

# function to open file and delete first line
def openingFile(fileName):
    myFile = open(fileName)
    myFile.readline()
    return myFile


# open file
myFile = openingFile("PowerBall.csv")
winningNumbersDict = dict()


# create dictionary with keys as winning number and values as the amount of times drawn
for line in myFile:
    items = line.split(",") # create a list of each line with items split by comma
    winningNumbers = items[1] # items at index 1 in each list are winning numbers
    winningNumbersSeperate = winningNumbers.split() # split the winning numbers on white space
    for value in winningNumbersSeperate: # for every number in each winning number
        if value not in winningNumbersDict: # if the value is not seen in the dictionary
            winningNumbersDict[value] = 1 # create new key starting at value 1
        else:
            winningNumbersDict[value] += 1 # add to exisitng key and increase value by 1


# sort the power ball numbers in descending order of their appearance frequency
compare = list() # list with key and value reversed
descendingList = list() # sorted list

for key,value in winningNumbersDict.items(): # for every key and value in the dictonary
    compare.append((value,key)) # append the items in the list in reverse (value, key)

while len(compare) != 0: # while the list has items (does not equal 0)
        maxValue = max(compare) # maxValue is the maximum value in the compare list
        descendingList.append(maxValue) # append maxValue into the descending list
        compare.remove(maxValue) # delete the maxValue from compare list

# print 10 most and least frequently drawn numbers
print("The 10 most frequent numbers are :")
for items in descendingList[:10]: # for every item up to index 10 in the list
    print(f"{items[1]} was drawn {items[0]} times.") # print key then value (number then amount of times drawn)

print("\nThe 10 least frequent numbers are :")
for items in descendingList[:-10:-1]: # for every item counting backwords up to index -10 in the list
    print(f"{items[1]} was drawn {items[0]} times.") # print key then value(number then amount of times drawn)
    
# End of Program

