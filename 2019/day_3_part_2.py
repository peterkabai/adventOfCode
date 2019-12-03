# https://adventofcode.com/2019/day/3

points_in_line = [[],[]]
distances = [[],[]]

for i, line in enumerate(open('inputs/day_3.txt')):
    pos = (0,0)
    total_dist = 0
    inputs = line.rstrip('\n').split(',')
    
    for inst in inputs:
        direction = inst[0]
        for step in range(1,int(inst[1:])+1):
            total_dist += 1
            distances[i].append(total_dist)
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
    dist = distances[0][points_in_line[0].index(point)] + distances[1][points_in_line[1].index(point)]
    smallest_dist = min(dist, smallest_dist)

print(smallest_dist)
        