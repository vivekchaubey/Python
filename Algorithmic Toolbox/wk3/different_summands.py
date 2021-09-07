# Uses python3
import sys


def split(a, num):
    return a, num - a


def get_change(n):
    output = []
    if n <= 2:
        print(1)
        print(n)
        return
    else:
        num = 1
        while True:
            num, remaining = split(num, n)
            if num < remaining:
                output.append(num)
                num = output[-1] + 1
            else:
                num = num + remaining
                output.append(num)
                break
            n = remaining
    print(len(output))
    answer = " ".join([str(each) for each in output])
    print(answer)
    return


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
