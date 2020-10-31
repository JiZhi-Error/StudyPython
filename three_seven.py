if __name__ == '__main__':
    a = int(input('第一个整数'))
    b = int(input('第二个整数'))
    if a % 2 != 0:
        print('第一个数为奇数', end='\n')
        print(a - b)
    else:
        print('第一个数为偶数', end='\n')
        print(a + b)
