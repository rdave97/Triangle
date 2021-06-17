values = [list(map(int, string.split()))for string in open('triangle.txt').readlines()]

for line in range(len(values)-1, 0, -1):
    for column in range(0, line):
        values[line-1][column] += max(values[line][column], values[line][column+1])

print("Maximum total from top to bottom in given triangle is", values[0][0])

