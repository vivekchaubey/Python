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


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
