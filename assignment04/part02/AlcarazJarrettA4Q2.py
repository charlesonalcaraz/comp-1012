""" AlcarazJarrettA4Q2

COMP 1012 Section A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 4, Question 2
AUTHOR: Charleson Jarrett Alcaraz
VERSION: 2020-Dec-02

PURPOSE: Create a program that wil place streets up for repair in list ordered by priority
         and determine which streets can be reparied with the given budget.
"""

# declare constants
COST_PER_KM = 1400000
FUNDING_AVAILABLE = 40000000

# street class
class Street:
  
    def __init__(self, name, length, carsperday, condition):
        self.name = name
        self.length = length
        self.carsperday = carsperday
        self.condition = condition
    
    def __str__(self):
        return f"{self.name} is {self.length}km long, sees {self.carsperday} cars per day, and is in {self.condition} condition."
        
    def compare(self, otherstreet):
        # return true if otherstreet is higher priority than first street
        output = False
        
        if self.condition == otherstreet.condition:
            if self.carsperday < otherstreet.carsperday:
                output = True
        elif self.condition == "fair" and otherstreet.condition == "poor":
            output = True
        elif self.condition == "good" and (otherstreet.condition == "poor" or otherstreet.condition == "fair"):
            output = True
            
        return output

    def getCost(self):
        # return cost to repair street
        return self.length * COST_PER_KM

# create beginning of bubble sort function (shift)
def bubbleSort(data):
    
    # if street b is higher priority than street a, switch
    for i in range(1,len(data)):
        a = data[i-1]
        b = data[i]
        if a.compare(b) == True:
            data[i-1] = b
            data[i] = a

# function that will open a file prompted from user, and create a corresonponding object
def streetSort():
    
    fileName = input("Enter file name : ")
    streets = open(f"{fileName}.txt")
   
    listOfStreets = list()
    unsortedList = list()

    # create a list where each entry is a street and its given properties
    for line in streets:
        line = line.strip()
        singleStreet = line.split(",")
        listOfStreets.append(singleStreet)
        
    # create a street object for each street and append each object into a list
    for data in listOfStreets:
        newStreet = Street(data[0], float(data[1]), float(data[2]), data[3])
        unsortedList.append(newStreet)

    # sort the list street objects ordered by repair priority
    for i in range(len(unsortedList)):
        bubbleSort(unsortedList)

    return unsortedList

# function that will print a list of streets that can be repaired with available money
def repairableStreets(sortedList, availableFunds):
    
    repairableStreets = list()
     
    # subtract cost to repair for each street from availableFunds and append to repair list
    for i in range(len(sortedList)):
        price = sortedList[i].getCost()
        availableFunds -= price
        repairableStreets.append(sortedList[i])
        
        # if cost goes negative, remove street from repair list and re-add cost to available funds
        if availableFunds > 0:
            repairableStreets.remove(sortedList[i])
            price += sortedList[i].getCost()
        
    return repairableStreets



# Main Line 
sortedStreets = streetSort()
repairableStreets = repairableStreets(sortedStreets, FUNDING_AVAILABLE)

print("\nThe streets in decreasing order of priority are :")
print("----------------------------------------------------")
for streets in sortedStreets:
    print(streets)
    
print("\nThe streets to be reparired are :")
print("----------------------------------------------------")
for i in range(len(repairableStreets)):
    print(f"{repairableStreets[i].name} will be repaired at a cost of ${repairableStreets[i].getCost():.2f}")

# End of Program

    

