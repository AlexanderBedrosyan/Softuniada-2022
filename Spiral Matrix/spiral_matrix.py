rows = int(input())
column = int(input())

matrix = []
directions = {"right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0]}

for i in range(rows):
    line = [ch for ch in input().split(" ")]
    matrix.append(line)

current_step = ["right", "down", "left", "up"]
position = [0, 0]
checker = 0
result = [matrix[0][0]]
matrix[0][0] = None

while True:
    step = current_step.pop(0)

    while True:
        row = position[0] + directions[step][0]
        col = position[1] + directions[step][1]
        if 0 <= row < rows and 0 <= col < column:
            if matrix[row][col] == None:
                checker += 1
                break
            checker = 0
            result.append(matrix[row][col])
            matrix[row][col] = None
            position = [row, col]
        else:
            checker += 1
            break
    current_step.append(step)
    if checker == 4:
        break

print(' '.join(result))
