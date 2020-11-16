if __name__ == '__main__':
    x = input('请输入一个大写字母：')
    i = ord(x)
    print('对应的小写字母为：{}'.format(chr(i + 32)))
