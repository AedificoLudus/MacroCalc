from itertools import product
from math import *
from dictionary import foods

amountOfFoods = len(foods) #how many types of food are there
amounts = [0, 0] #amounts of each food
results = [] #resulting diets

target = [0, 0, 0] #put target macros here - protein, carb, fat
tolerance = 0 #tolerance allowed for macros
maxFood = 0 #how much of any 1 food is allowed
portions = 100 #how big are the increments?
maxPortions = 5 #how many portions are allowed


def intput(msg): #Remember 04/11/2013
    return int(input(msg))

def calcMacros (amounts, foods):
    macros = [0, 0, 0]
    if sum(amounts) < 20:
        for i in range(len(amounts)):
            macros[0] += amounts[i]*foods[i][1] #add protein
            macros[1] += amounts[i]*foods[i][2] #add carbs
            macros[2] += amounts[i]*foods[i][3] #add fats
    return macros

def checkMacros (target):
    for i in product(range(maxPortions), repeat=amountOfFoods): #iterate over each possible permutation
        check = calcMacros(i, foods) #get the macros for this permutation
        if (target[0]-tolerance < check[0] < target[0]+tolerance and #check protein
            target[1]-tolerance < check[1] < target[1]+tolerance and #check carbs
            target[2]-tolerance < check[2] < target[2]+tolerance): #check fats
            results.append(i) #add succesful permutations to the results
            print("Valid Result Found")

while True:
    print("All numbers are in grams")
    tolerance = intput("How much tolerance is allowed? ")
    target[0] = intput("How much protein do you want? ")
    target[1] = intput("How much carbs do you want? ")
    target[2] = intput("How much fat do you want? ")
    print('Macros Input')
    checkMacros(target)
    print(results)
    print (str(len(results)) + 'different options returned')
