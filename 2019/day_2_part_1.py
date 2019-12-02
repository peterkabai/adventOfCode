# https://adventofcode.com/2019/day/1

with open('day_2_input.txt', 'r') as f: code = f.read()
codes = [int(s) for s in code.split(',')]

codes[1] = 12
codes[2] = 2

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

print(codes[0])