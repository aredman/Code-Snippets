# Script to compute pi using the monte carlo method
# Andrew Redman
# 12/06/2021

import math
import random

# Determine output frequency (number of loops)
n_output = 1e6

# Count number of 'hits' and loops
count = 0
n_loops = 0

# Can restart from previous 'save' point by entering 'count' and 'loop' values
#count = 224618261
#n_loops = 286000000

while(True):
    # Increment counter
    n_loops += 1

    # Get random X,Y pair within unit square
    x = random.random()
    y = random.random()
    
    # Check if values are within unit circle
    distance = math.sqrt(x**2 + y**2)
    if(distance <1):
        count +=1

    # Compute pi every n_output loops
    if(n_loops % n_output == 0 ):
        pi = 4 * count / n_loops
        print("4* " + str(count) +" / " + str(n_loops) + " =\t" + str(pi))
