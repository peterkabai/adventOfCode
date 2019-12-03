# https://adventofcode.com/2019/day/3


points_in_line = [[],[]]
for i, line in enumerate(open('inputs/day_3.txt')):

    pos = (0,0)

    inputs = line.rstrip('\n').split(',')
    for inst in inputs:
        direction = inst[0]
        distance = int(inst[1:])

        for step in range(1,distance+1):
            if direction == "R":
                pos = (pos[0], pos[1]+1)
            elif direction == "L":
                pos = (pos[0], pos[1]-1)
            elif direction == "U":
                pos = (pos[0]+1, pos[1])
            elif direction == "D":
                pos = (pos[0]-1, pos[1])
            points_in_line[i].append(pos)
smallest_dist = float('Inf')

matching_points = set(points_in_line[0]) & set(points_in_line[1])

for point in matching_points:
    dist = abs(point[0])+abs(point[1])
    smallest_dist = min(dist, smallest_dist)

print(smallest_dist)
        