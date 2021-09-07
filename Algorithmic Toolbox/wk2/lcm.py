# Uses python3
import sys


def gcd_naive(aa, bb):
    if aa == 0:
        return bb
    elif bb == 0:
        return aa
    elif aa == bb:
        return aa
    elif aa > bb:
        return gcd_naive(aa % bb, bb)
    elif bb > aa:
        return gcd_naive(aa, bb % aa)


def lcm_naive(aaa, bbb):
    lcm = (aaa * bbb) / gcd_naive(aaa, bbb)
    return int(lcm)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))
