# Uses python3
import sys


def get_change(m):
    # write your code here
    output = []

    while m>0:
        if m%10 == 0:
            output.append(10)
            m=m-10
        elif m%5 ==0:
            output.append(5)
            m=m-5
        else:
            output.append(1)
            m=m-1
    return len(output)


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
