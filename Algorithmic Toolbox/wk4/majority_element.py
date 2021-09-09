# Uses python3
import sys
from collections import Counter


def get_majority_element(x):
    me = x[0]
    count = 1
    for each in x[1:]:
        if each == me:
            count += 1
        else:
            count -= 1
            if count == 0:
                me = each
                count = 1
    if count == 1:
        return -1
    else:
        counter = 0
        for each in x:
            if each == me:
                counter += 1
        if counter > len(x) / 2:
            return 1
        else:
            return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    if get_majority_element(input_keys) != -1:
        print(1)
    else:
        print(0)
