# Uses python3
import sys
import math


def get_change(money):
    # write your code here
    coins = [1, 3, 4]
    minCoins = [0] + [math.inf] * money
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                count = minCoins[m - coin] + 1
                if count < minCoins[m]:
                    minCoins[m] = count
    return minCoins[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
