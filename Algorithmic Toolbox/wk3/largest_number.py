# Uses python3

import sys


def arrange_correct(a, b):
    aa = int(str(a) + str(b))
    bb = int(str(b) + str(a))
    if aa > bb:
        return True
    else:
        return False


def largest_number(lst):
    answer = []
    while len(lst) != 0:
        currentmax = 0
        for each in lst:
            check = arrange_correct(each, currentmax)
            if check:
                currentmax = each
            else:
                continue
        answer.append(currentmax)
        lst.remove(currentmax)

    return "".join([str(each) for each in answer])


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    print(largest_number(a))
