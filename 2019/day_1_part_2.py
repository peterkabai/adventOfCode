# https://adventofcode.com/2019/day/1

import math

total_fuel = 0
for line in open('inputs/day_1_input.txt'):
    mass = int(line.rstrip('\n'))
    while mass > 0:
        mass = math.floor(mass/3)-2
        total_fuel += mass if mass > 0 else 0

print(total_fuel)