""" AlcarazJarrettA2Q2

COMP 1012 SECTION A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 2, Question 2
AUTHOR: Charleson J. Alcaraz
VERSION: 2020-Oct-26

PURPOSE: Create a program that decrypts a file.

PSEUDOCODE:

prompt user for input (the file to decrypt)
open the file 

create a dictionary that will track frequency of characters
for every line in the opened file
    for every character in the line
        if the character is not "\n" (enter character)
            if the character is not already in the dictionary
                add it to the dictionary
            if the character is already in the dictionary
                increase it's value (frequency) by 1

create a list for characters over frequency 10
for every key and value in the frequency dictionary
    if the value is greater than 10
        append it to the list as a tuple the value first and the key second 

create a list that will be the sorted version of the list with characters over frequency 10
while the lengh of the list with characters over frequency 10 is not 0
    for every value-key tuple in the list with characters over frequency 10
        find the maximum value in the list
        append the key from the tuple to the new list (sorted list)
        delete this maxmimum value/tuple from the old list (char over freq 10 list)

number of characters is the length of the ordered list
shift variable is the number of characters minus 9
create a dictionary that will be our cipher
for every encrypted index and encrypted character in the enumerated versoin of the ordered list
    the decrypted index is the encrypted index plus the shift, and modulus number of characters
    the decrypted character is the ordered list indexed at its decrypted index
    the key of cipher is the encrypted character and the value is the decrypted character
    
re-open the file
create an empty string
for every line in the opened file
    for every character in every line
        if the character is in the cipher
            the encrypted character is switched to its corresponding decrypted character in the cipher 
            decrypted character is the new switched encrypted character
            append the decrypted character to the empty string
        else (character is not in the cipher)
            encrypted character remains unchanged
            append the unchanged character to the empty string

print the string

"""


# prompt user for file to decrypt (write only file name, do not include '.txt' 
file = input("Please enter the file you wish to decrypt: ")
openedFile = open(f"{file}.txt")


# create a dictionary with keys as the letter seen in the file and the value as their frequency within the file
frequencyDict = dict() # letter-frequency dictionary
for line in openedFile: # for every line in the file
        # print(line)
    for character in line: # for every character in every line
        # print(character)
        if character != "\n": # do not include \n (enter)
            if character not in frequencyDict: # if the character has not been seen
                    frequencyDict[character] = 1 # create new key with value 1
            else: # if the letter has been seen
                    frequencyDict[character] += 1 # add 1


# sort the dictionary so that will create a list of the characters with >10 frequency
overTen = list() # list of characters with over frequency 10
for key, value in frequencyDict.items(): # for every key and value in the dict
    if value > 10: # if the value is greater than ten (letter appears more than ten times)
        # print(f"key is {key} value is {value}")
        overTen.append((value,key))
        # print(overTen)

# sort the list list with character >10 frequency in a descending fashion
descendingList = list() # descending ordered list
while len(overTen) != 0: # while the length of the list does not equal 0
    for pair in overTen: # for every pair (value, key) in the list with characters over frequency 10
        maxVal = max(overTen) # maxVal is the maximum value in that list
        # print(maxVal)
        descendingList.append(maxVal[1]) # append maxVal into the descending list
        overTen.remove(maxVal) # delete the maximum value from original list of characters with over frequency 10

# create a cipher that will match characterse with their corresponding shifted/decrypted characters
numChars = len(descendingList) # number of characters
shiftVar = numChars - 9 # shift variable
cipher = dict() # cipher map
for encryptedIndex,encryptedChar in enumerate(descendingList): # for every encrypted index and encrypted character in the enumerated list
    decryptedIndex = (encryptedIndex + shiftVar) % numChars # the decrypted index is the encryped index plus the shiftVar and modulus of numChars
    decryptedChar = descendingList[decryptedIndex] # decrypted character is the list indexed at the new decrytped index (shifted index)
    cipher[encryptedChar] = decryptedChar # cipher key is encrypted character, value is decrypted character


# print the decrypted file
openedFile = open(f"{file}.txt")
decryptedText = "\n" # final decrypted string
for line in openedFile: # for every line in the file
    for encryptedCharacter in line: # for every encrypted character in the line
        if encryptedCharacter in cipher: # if the encrypted character is in the cipher
            encryptedCharacter = cipher[encryptedCharacter] # change encrypted character to its corresponding decrypted character
            decryptedCharacter = encryptedCharacter # decrpyted character
            decryptedText += decryptedCharacter # concatenate to string
        else:
            encryptedCharacter = encryptedCharacter # character remains the same if not in cipher
            decryptedText += encryptedCharacter # concatenate to string
    
print(decryptedText)

# End of Program
