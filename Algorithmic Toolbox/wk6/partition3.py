# Uses python3
import sys
import itertools


def findgroups(a, n, summ):
    sumset = {0}
    for each in a:
        possibles = []
        for eachsum in sumset:
            num = eachsum + each
            possibles.append(num)
        sumset.update(possibles)
        if summ in sumset:
            return True
    return False


def partition3(a):
    n = 3
    summ = sum(a) / n
    if summ.is_integer():
        summ = int(summ)
        bool=findgroups(a, n, summ)
        if bool:
            return 1
        else:
            return 0
    else:
        return 0
    return a


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(partition3(A))
