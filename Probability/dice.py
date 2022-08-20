#!/usr/bin/python
# Pick dice
print("Importing libraries")
import numpy as np

Dice = [6,6]
Rolls = []
Probability = []

min_roll =len(Dice)
max_roll = sum(Dice)


outcomes = 1
for die in Dice:
    outcomes = outcomes * die
    Rolls.append(list(range(1,die+1)))

print(f"Min Roll: {min_roll}")
print(f"Max Roll: {max_roll}")
print(f"Outcomes: {outcomes}")

Results = np.array([])
count = 0
for die in Rolls:
    count = count + 1
    new_results = np.array([])
    if(Results.size == 0):
        new_results = np.array(die)
    else:
        for d in die:
            for r in Results:
                new_results = np.append(new_results,d+r)
    Results =  new_results

Results.sort()
Unique = np.unique(Results)
