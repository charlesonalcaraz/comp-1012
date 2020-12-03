""" AlcarazJarrettA4Q1

COMP 1012 Section A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 4, Question 1
AUTHOR: Charleson Jarrett Alcaraz
VERSION: 2020-Dec-01

PURPOSE: Create a program that will read a set of data points from a file and find 
         the best fit line to the data, and plot the data in line.
"""

# perform imports
import numpy as np
import matplotlib.pyplot as plt

# function that will prompt user for file and open it
def openFile():
    fileName = input("Enter file name : ")
    return open(f"{fileName}.txt")

# function that will create a 2D array of the points in the file
def fill2DArray(data):
   pointsList = list()
    
   for line in data:
       line = line.strip()
       points = line.split(",")
       pointsList.append(points)
    
   pointsArray = np.array(pointsList, dtype = np.float64)
   return pointsArray

# function that will perform least square method and graph it
def leastSquareMethod(array):
    # retreive x coordinates and y coordinates
    xCoords = array[:,0]
    yCoords = array[:,1]
    
    # calculate mean of X and Y 
    xMean = np.mean( xCoords )
    yMean = np.mean( yCoords )
    
    # calculate slope
    slope = (((xCoords - xMean)*(yCoords - yMean)).sum()) / ((xCoords - xMean) ** 2).sum()
    
    # calculate y-intercept
    b = yMean - slope * xMean
    
    # plot the function and the original points
    plt.scatter( xCoords, yCoords, c = "k")
    plt.plot(xCoords, slope * xCoords + b, c = "k")
    
    return f"\nThe equation of the slope is y = {slope:.2f}x + {b:.2f}"


# Main line
dataFile = openFile()
dataArray = fill2DArray(dataFile)
print(leastSquareMethod(dataArray))


# End of Program
