# https://adventofcode.com/2019/day/1

import math

total_fuel = 0
for line in open('inputs/day_1_input.txt'):
    mass = int(line.rstrip('\n'))
    fuel = math.floor(mass/3)-2
    total_fuel += fuel

print(total_fuel)