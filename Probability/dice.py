#!/usr/bin/python
# Pick dice
print("Importing libraries")
import numpy as np
import matplotlib.pyplot as plt

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

Unique = np.unique(Results)
for i in Unique:
	prob = np.count_nonzero(Results==i)/outcomes
	Probability = np.append(Probability, prob*100)

	print(f"{i}:\t{round(prob*100,2)}%")
Unique = Unique.astype(int)

figure, ax  = plt.subplots()
p1 = ax.bar(Unique,np.round(Probability,2))
ax.set_title(f"Dice Rolled: {Dice}")
ax.set_xlabel("Roll")
ax.set_ylabel("Probability (%)")
#ax.bar_label(p1,Unique,label_type="center")
ax.bar_label(p1,np.round(Probability,2))
ax.set_ylim([0,27])
plt.xticks(Unique,Unique)

filename = "Roll"
for i in Dice:
	filename = f"{filename}_{i}"
filename = filename + ".png"

plt.savefig(filename)
