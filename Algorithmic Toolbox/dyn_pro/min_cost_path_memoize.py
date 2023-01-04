# use memoization to solve minimum cose ptoblem

import numpy as np

# define input matrix
min_val, max_val, rows, cols = 1, 15, 4, 5
inp = np.random.randint(min_val, max_val, size=(rows, cols))
print(inp)
output = np.zeros((rows, cols))
memoization = {}

for row in range(rows):
    for col in range(cols):
        if row == 0 and col == 0:
            memoization[(row, col)] = inp[row][col]
        elif row == 0:
            memoization[(row, col)] = inp[row][col] + memoization[(row, col-1)]
        elif col == 0:
            memoization[(row, col)] = inp[row][col] + memoization[(row-1, col)]
        else:
            memoization[(row, col)] = inp[row][col] + min(memoization[(row-1, col)], memoization[(row, col-1)])
        output[row][col] = memoization[(row, col)]

print("SHORTEST PATH DETAILS------->")
print(output)
print(memoization[(rows-1, cols-1)])

