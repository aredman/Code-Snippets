#!/usr/bin/python
# Pick dice

Dice = [4,4,6]
Rolls = []
Probability = []

min_roll =len(Dice)
max_roll = sum(Dice)

print(f"Min Roll: {min_roll}")
print(f"Max Roll: {max_roll}")


outcomes = 1
for die in Dice:
    outcomes = outcomes * die
    Rolls.append(list(range(1,die+1)))

#print(Rolls)

print(f"Outcomes: {outcomes}")

Results = []
for die in Rolls:
    new_results = []
    if(Results == []):
        new_results = die
    else:
        for d in die:
            for r in Results:
                new_results.append( d+r)
    Results = new_results

#print(Results)
Results.sort()
print(Results)
