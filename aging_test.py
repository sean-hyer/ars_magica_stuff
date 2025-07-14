'''
The way aging works in Ars Magica:
Every year once you turn 35:
Roll a stress die (no botch)
Add your age/10 (round up)
Subtract any modifiers
If the result is a 13 or 22+, gain a decrepitude (a point of aging: you die at 5)
'''

import random
import math

num_tries = 10000

def stress_roll():
    '''This function rolls a stress die and returns the result.
    If the stress die multiplies, it calls a second function for recursion.'''
    roll = random.randint(1, 10)
    if roll == 10:
        return 0
    elif roll == 1:
        roll = multiply_roll(2)
    return roll


def multiply_roll(multiplier):
    '''This function implements stress die explosion'''
    roll = random.randint(1, 10)
    if roll == 1:
        roll = multiply_roll(multiplier*2)
        return (roll)
    else:
        return (roll*multiplier)


def aging(modifier):
    age = 34
    decrepitude = 0
    while decrepitude < 5:
        age += 1
        aging_roll = stress_roll() + math.ceil(age/10) - modifier
        if aging_roll == 13 or aging_roll >= 22:
            decrepitude += 1
    return age

# Right now I'm not using this.
# It might be useful later but I'm looking at averages not distributions.
age_grid = []
for i in range(0, 300):
    age_grid.append([(i), (0)])

sum_ages = 0
for i in range(1, num_tries):
    result = aging(8)
    age_grid[result][1] += 1
    sum_ages += result

print(age_grid)
print(f"the average age at death was {sum_ages / num_tries}")
