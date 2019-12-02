# https://adventofcode.com/2019/day/2

import copy

with open('inputs/day_2_input.txt', 'r') as f: code = f.read()
code_initial = [int(s) for s in code.split(',')]

for i in range(0,99):
    for j in range(0, 99):
        codes = copy.deepcopy(code_initial)
        codes[1] = i
        codes[2] = j

        optcode_pos = 0

        while True:
            opt_code = codes[optcode_pos]
            if opt_code == 1:
                codes[codes[optcode_pos + 3]] = codes[codes[optcode_pos + 1]] + codes[codes[optcode_pos + 2]]
            elif opt_code == 2:
                codes[codes[optcode_pos + 3]] = codes[codes[optcode_pos + 1]] * codes[codes[optcode_pos + 2]]
            else:
                break

            optcode_pos += 4

        if codes[0] == 19690720:
            print(i, j)