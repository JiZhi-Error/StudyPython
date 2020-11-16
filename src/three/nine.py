import math


def finish_count(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    sum = 0
    for i in range(2,1001):
        if finish_count(i):
            sum += 1
            print(i)
    print('完数个数为：', sum)
