""" AlcarazJarrettA1Q1

COMP 1012 Section A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 1, Question 2
AUTHOR: Charleson Jarrett Alcaraz
VERSION: 2020-Oct-12

PURPOSE: Create a program that will take user input of coordinates and calculate the linear connection between the points
"""
        
  
# prompt user for 2 sets (x, y) coordinates
x1Str = input("Enter a value for x1 : ") 
y1Str = input("Enter a value for y1 : ")
x2Str= input("Enter a value for x2 : ")
y2Str= input("Enter a value for y2 : ")

# convert (x, y) coordinates into floats
x1 = float(x1Str)
y1 = float(y1Str)
x2 = float(x2Str)
y2 = float(y2Str)

# equation to calculate slope (y = mx + b)
slope = (y2 - y1) / (x2 - x1)
b = y2 - (slope * x2) 
print("y = mx + b, y = {:.2f}x + {:.2f}".format(slope, b))

# prompt user for command to commence if-loop iteration
print("\nWould you like to enter coordinates or return a set of coordinates?")
command = input("Enter either one of the following :\nx , y, set : ")

# will use the counter to increase the index by increments of 2 up until +10
counter = 0 
index = -10

if command == "x" : # if user enters x
    xPrompt = input("Enter a coodinate for x : ") # ask user to input value for x
    xNumber = float(xPrompt) # convert input into numerical value
    y = (slope * xNumber) + b # substitute user value of x into slope equation to recieve y
    print("Your coordinate set is ({:.2f} , {:.2f})".format(xNumber, y)) # print user value of x and newly calulated y
elif command == "y" : # if user enters y
    yPrompt = input("Enter a coordinate for y : ") # ask user to input value for y
    yNumber = float(yPrompt) # convert input into numerical value
    x = (yNumber - b) / slope # substitute user value of y into slope equation to recieve x
    print("Your coordinate set is ({:.2f},{:.2f})".format(x, yNumber)) # print user value of y and newly calulcated x
elif command == "set" : # if user enters set
    while -10 <= counter < 10 : # while the value of counter/x is lesser or equal to -10 and lesser than 10
        counter = index # equate counter/x to index so the commenced while loop will let counter/x = -10
        yValue = (counter * slope) + b # calculating y using the value of the counter/x; using slope equation
        yValueNumber = float(yValue) # convert y into numerical value 
        print("({:.2f},{:.2f})".format(counter, yValueNumber)) # print counter/x value and new value of y
        index += 2 # increase the counter/x by 2 and restart while loop
else : # if user enters anything besides x, y, or set
    print("Incorrect Command. Please try again.")
        
# End of Program






















