""" AlcarazJarrettA3Q1

COMP 1012 SECTION A02
INSTRUCTOR: Heather Matheson
ASSIGNMENT: Assignment 3
AUTHOR: Charleson J. Alcaraz
VERSION: 2020-Nov-17

PURPOSE: Write a function that simulates a single trial to calculate the lifespan of 
         a colony of amoebas, given their chance of survival. Following that, you will
         run that trial for some number of repeated trials.
"""

# Declare Constants
AMOEBAS = 1
SURVIVAL = 0.50
MAXSURVIVAL = 1.00
SIMULATIONS = 1000

# perform imports
import numpy as np

# create a function that will calculate the next generations for the amoeba population
def nextGen(numOfAmoebas, oddsOfSurvival):
    populationList = list()
    
    # create an array the size of the amount of amoebas, with random float (odds) representing each of them
    for amoeba in range(0, numOfAmoebas):
        randomOdds = np.random.uniform(0,1)
        populationList.append(randomOdds)
        
    #convert population list into an array, use survival odds and array slicing to kill off ameobas
    populationArray = np.array(populationList)
    
    # kill off some alive amoebas using survival odds, and duplicate every amoeba that survived
    aliveAmoebas = populationArray[populationArray < oddsOfSurvival]
    offSpring = len(aliveAmoebas) * 2
    
    return offSpring
    
    
# create a function that executes a single trial of the amoeba experiment
# will return number of iterations simulated, boolean if all amoebas are dead before 20 gens, and the final pouplation
def singleTrial(Amoebas, Survival):
    
    # inital generation
    genCounter = 1
    
    # while there is not 20 generations and total of amoebas is not 0 (not all dead)
    while genCounter < 20 and bool(Amoebas != 0):
        genCounter += 1
        Amoebas = nextGen(Amoebas, Survival)
    
    # will return total generations, TRUE if amoebas survived all 20 gens, and total Amoebas survived)
    # print(f"total successful generations was {genCounter} gens, with a remaining {totalAmoebas} amoebas.")
    return (genCounter, bool(Amoebas != 0), Amoebas)
    

# create a function that will repeat the single trial a given amount of times
def repeatTrial(simulations, Amoebas, Survival):
    
    # create lists of data that will be converted into arrays
    totalGensSurvived = []
    survivalBoolean = []
    remainingAmoebas = []
    
    # append information from tuple into seperate lists
    for trials in range(0, simulations):
        Trial = singleTrial(Amoebas, Survival)
        totalGensSurvived.append(Trial[0])
        survivalBoolean.append(Trial[1])
        remainingAmoebas.append(Trial[2])
        
    # convert lists into array
    totalGensArray = np.array(totalGensSurvived) 
    survivalBooleanArray = np.array(survivalBoolean)
    remainingAmoebasArray = np.array(remainingAmoebas)
    
    # calculate percentage of failed colonies
    totalFailedColonies = len(remainingAmoebasArray[remainingAmoebasArray == 0])    
    survivalPercentage = totalFailedColonies / len(remainingAmoebasArray) * 100
   
    # calculate average failed generations
    totalFailedGens = totalGensArray[survivalBooleanArray == False]
    avgFailedGens = np.mean(totalFailedGens)
    
    # calculate avg population for succesful populations
    successfulPopulations = remainingAmoebasArray[survivalBooleanArray == True]
    avgSuccessfulPop = np.mean(successfulPopulations)
    
    return (survivalPercentage, avgFailedGens, avgSuccessfulPop)


# Main Line 
while SURVIVAL < MAXSURVIVAL:
    print(f"For Survival Odds of {SURVIVAL:.2f}:")
    trials = repeatTrial(SIMULATIONS, AMOEBAS, SURVIVAL)
    print(f"  The Amoebas did not survive {trials[0]:.2f}% of the time.")
    print(f"  On failures, there were {trials[1]:.2f} generations on average.")
    print(f"  The average population was {trials[2]:.2f} if the amoebas did survive.\n")
    SURVIVAL += 0.05

print("Done")


# End Of Program
# Note: Program takes quite a bit of time to run through



