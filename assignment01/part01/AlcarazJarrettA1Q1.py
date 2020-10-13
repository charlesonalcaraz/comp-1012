""" AlcarazJarrettA1Q1

COMP 1012 Section A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 1, Question 1
AUTHOR: Charleson Jarrett Alcaraz
VERSION: 2020-Oct-12

PURPOSE: Create a program that calculates estimates on how long it would take a user to re-type a book
"""


# Initializing the Program
# This block of code will complete the following :
#       1) Prime the user's input until it matches the desired input (proper book title))
bookPrompt = input("What book would you like to read? : ") # prompt user for input 

while not bookPrompt == "Relativity" : # program will not begin until user enters book title 'Relativity'
    bookPrompt = input("That book is not in our files. Please choose another : ") # if input is not 'Relativity' , ask for more input
file = open("Relativity.txt") 


# Random Line Selector
# This block of code will complete the following :
#       1) Choose a random line with 10 or more characters on it
file = open("Relativity.txt")
import random 
list = [] # list of lines/strings with 10 characters or more

for line in file: # for every line in the book
    if len(line) >= 10: # if the length of the line is greater or equal to 10 characters
        list.append(line) # insert line (string) into list
    randomLine = random.choice(list) # choose any one of those strings in the list randomly

# User Re-Type of Random Line
# This block of code will complete the following :
#       1) Prompt the user to retype a random line chosen from the book
#       2) Calcuate the user's Words per Minute and Charcters per Minute given the time it took 
import time

print("\nWe are now going to time how fast you can re-type a given line from the book...")

userTimeIntializer = input("Press enter when you are ready to start : ") # timer will begin when user presses enter
startTime = time.time() # start time from January 1st, 1970 in seconds
userRetype = input("Type \"{}\" : ".format(randomLine))
totalTime = time.time() # end time (present) in seconds
timeInterval = (totalTime - startTime) / 60 # converting total time from seconds into minutes

wordsInLine = len(randomLine.split()) # total words in the given random line
charactersInLine = len(randomLine) # total charcters in the given random line
charactersPerMin = charactersInLine / timeInterval # total characters divided by total time in minutes
wordsPerMin = wordsInLine / timeInterval # total words divided by total time in minutes

if timeInterval < 0.15: # if time interval is within certain time range, print the following
    print("\nYou didn't type that you're a bot! Your total time was {:.2f} minutes?!".format(timeInterval))
else : # if time interval is not within certain time range, print the following
    print("\nYou didn't take all the right type when you were younger.. your total time was {:.2f} minutes.".format(timeInterval))

print("\nGiven that there were {:.2f} characters and {:.2f} words...".format(charactersInLine, wordsInLine))
print("You typed at {} characters per minute.".format(charactersPerMin))
print("You typed at {} words per minute.".format(wordsPerMin))


# Character and Word Statistics
# This block of code will complete the following :
#       1) Calculate the total amount of of characters in the book 
#       2) Calculate the total amount of words in the book
file = open("Relativity.txt")
characterCount = 0 # total sum of characers in the book
wordCount = 0 # total sum of words in the book

for line in file: # for every line in the book
    # chacter calculation
    characterCount = len(line) + characterCount # add the amount of characters in each line to total sum
    # word calculation
    words = line.split() # list of words in each line
    wordCount = len(words) + wordCount # add the amount of words in each line to total sum
    
print("\nThis book has {} characters and {} words.".format(characterCount, wordCount))


# Average Word Length
# This block of code will complete the following :
#       1) Calulate the average word length in the book by :
#           - taking the total sum the length of every word
#           - taking that sum and dividing it by the total amount of words
file = open("Relativity.txt")
lengthOfWords = 0 # total sum of the length of every word in the book
totalWords = 0 # total sum of all the words in the book

for line in file: # for every line in the book
    words = line.split() # list of words in each line
    totalWords = len(words) + totalWords # add the amount of words in each line to total sum 
    
    for word in words: # for every word in each list
        lengthOfWords = len(word) + lengthOfWords # add the length of each word in each list to total sum
        averageWordLength = lengthOfWords / totalWords # average word length is total length of every word divided by total amount of words

print("The average word length is {:.2f}".format(averageWordLength))


# Average Length of Lines
# This block of code will complete the following :
#       1) Calculate the average length of each line in the book by:
#           - taking the total sum of the length of every line
#           - taking that sum and dividing it by the total amount of lines 
file = open("Relativity.txt")
lengthOfLines = 0 # total sum of the length of every line in the book
totalLines = 0 # total amount of lines in the book

for line in file: # for every line in the book
    totalLines += 1 # increase the total amount of lines by 1
    strippedLine = line.strip() # strip white spaces from each line
    lengthOfLines = len(strippedLine) + lengthOfLines # add the length of every line to the total sum of the length of all the lines
    averageLineLength = lengthOfLines / totalLines # average line length is total sum of the length of every line the divided by the total amount of lines

print("The average length of each line is {:.2f}".format(averageLineLength))


# Total Blank Lines
# This block of code will complete the following :
#       1) Calculate the total amount of blank lines in the book
file = open("Relativity.txt")
totalBlanks = 0 # total blank lines

for line in file: # for every line in the book
    strippedLine = line.strip() # strip excess white spaces between lines
    sentenceSplit = strippedLine.split() # list of words in each line
    
    if sentenceSplit == []: # if list contains nothing (blank space)
        totalBlanks += 1 # increase the total amount of blanks by 1
        
print("The number of blanks lines is {}".format(totalBlanks)) 

# Hours for User to Re-Type Book
# This block of code will complete the following :
#       1) Using the calculated words per minute
#           - calculate in both hours and minutes the total time it would take the user to retype the book
#       2) using the calculated characters per minute
#           - calculate in both hours and minutes the total time it would take the user to retype the book
retypeWords = (totalWords / wordsPerMin) # total time for user to retype book in minutes (WPM)
retypeWordsHours = (totalWords / wordsPerMin) / 60 # total time for user to retype book in hours (WPM)
retypeCharacters = (characterCount / charactersPerMin) # total time for user to retype book in minutes (CPM)
retypeCharactersHours = (characterCount / charactersPerMin) / 60 # total time for user to retype book in hours (CPM)

print("\nIf you were re-typing Einsteins Theory of Relativity :")
print("It would take you {:.2f} minutes ({:.2f} hours) based on your calculated words per minute.".format(retypeWords, retypeWordsHours))
print("It would take you {:.2f} minutes ({:.2f} hours) based on your calculated characters per minute.".format(retypeCharacters,retypeCharactersHours))

print("End of Program")

# End of Program


        
    









    
        

        
    



        
        
        
            

    
    
    
    









