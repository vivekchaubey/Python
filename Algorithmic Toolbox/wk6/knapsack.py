# Uses python3
import sys
import math


def optimal_weight(W, w):
    # write your code here
    mat = [[math.inf] * (W + 1) for i in range(len(w) + 1)]
    mat[0] = [0 for each in mat[0]]

    for each in mat:
        each[0] = 0

    w.insert(0, 0)

    for weightindex in range(1, len(w)):
        for kweight in range(1, W + 1):
            if w[weightindex] == kweight:
                mat[weightindex][kweight] = kweight
            elif kweight < w[weightindex]:
                mat[weightindex][kweight] = mat[weightindex - 1][kweight]
            elif kweight > w[weightindex]:
                p = max(mat[weightindex - 1][kweight], mat[weightindex - 1][kweight - w[weightindex]] + w[weightindex])
                mat[weightindex][kweight] = p
    return mat[-1][-1]


if __name__ == '__main__':
    inp1=list(map(int, input().split()))
    assert len(inp1) == 2

    w = list(map(int, input().split()))
    assert len(w) == inp1[1]

    print(optimal_weight(inp1[0], w))
