if __name__ == '__main__':
    x = int(input('请输入3位正整数'))
    hundreds = x // 100
    ten = (x - (hundreds * 100)) // 10
    ones_place = x - (hundreds * 100) - (ten * 10)
    print('按逆序输出为：{}{}{}'.format(ones_place, ten, hundreds))
