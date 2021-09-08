# Uses python3

import sys
import math


def lcs2(x, y):
    x.insert(0, " ")
    y.insert(0, " ")

    lenx = len(x)
    leny = len(y)

    # Initializing the distance matrix
    mat = [[math.inf] * (leny) for i in range(lenx)]
    mat[0] = [0 for each in mat[0]]
    for each in mat:
        each[0] = 0

    for i in range(1, leny):
        for j in range(1, lenx):
            if y[i] == x[j]:
                mat[j][i] = 1 + mat[j - 1][i - 1]
            else:
                mat[j][i] = max(mat[j][i - 1], mat[j - 1][i])

    return mat[-1][-1]


if __name__ == '__main__':
    num_keys = int(input())
    aa = list(map(str, input().split()))
    assert len(aa) == num_keys

    num_queries = int(input())
    bb = list(map(str, input().split()))
    assert len(bb) == num_queries

    print(lcs2(aa, bb))
