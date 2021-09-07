# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n < 2:
        return n
    else:
        previous, current = 0, 1
        for each in range(2, n + 1):
            current, previous = (previous+current) % 10, current
        return current


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
