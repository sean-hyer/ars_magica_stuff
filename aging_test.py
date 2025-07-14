# so
# aging
# stress die (no botch)
# plus age/10 (round up)
# -  modifiers
# we'll ignore random point increases
# your age increases by 1 every time you roll a 13 or a 22+
# we'll assume medical care is always perfect and available

import random
import math


def stress_roll():
    roll = random.randint(1, 10)
    if roll == 10:
        return 0
    elif roll == 1:
        roll = multiply_roll(2)
    return roll


def multiply_roll(multiplier):
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


age_grid = []
for i in range(0, 300):
    age_grid.append([(i), (0)])

sum_ages = 0
for i in range(1, 10000):
    result = aging(8)
    age_grid[result][1] += 1
    sum_ages += result

print(age_grid)
print(f"the average age at death was {sum_ages / 10000}")
