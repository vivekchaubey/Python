# different possible paths in matrix. 1 means pass. 0 means stop

import numpy as np

# define input matrix
min_val, max_val, rows, cols = 0, 2, 4, 5
inp = np.random.randint(min_val, max_val, size=(rows, cols))
inp[0][0], inp[0][2], inp[3][1], inp[0][1], inp[1][1], inp[3][2], inp[rows-1][cols-1] = 1, 1, 1, 1, 1, 1, 1
print(inp)
output = np.zeros((rows, cols))
memoization = {}

for row in range(rows):
    for col in range(cols):
        if row == 0 and col == 0:
            output[row][col] = inp[row][col]
        elif row == 0:
            if inp[row][col] == 0:
                try:
                    output[row][col] = 0
                    inp[row][col+1] = 0
                except Exception as e:
                    pass
            else:
                output[row][col] = inp[row][col]
        elif col == 0:
            if inp[row][col] == 0:
                try:
                    output[row][col] = 0
                    inp[row+1][col] = 0
                except Exception as e:
                    pass
            else:
                output[row][col] = inp[row][col]
        else:
            if inp[row][col]!=0:
                output[row][col] = output[row-1][col]+output[row][col-1]
            else:
                output[row][col]=0

print("ways-------->")
print(output)
