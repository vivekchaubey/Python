# Uses python3
def calc_fib(n):
    if n < 2:
        return n
    else:
        previous, current = 0, 1
        for each in range(2, n+1):
            temp = current
            current = previous + current
            previous = temp
        return current



n = int(input())
print(calc_fib(n))
