while True:
    print('''1.\t字符串加密
2.\t字符串解密''')
    options = int(input('请输入选项(-1退出程序)：'))
    print()
    if options == -1:
        print('程序退出，欢迎下次使用')
        exit()
    elif options == 1:
        msg = input('请输入待加密字符串：')
        encryptMsg = ''
        for i in msg:
            ordChr = ord(i)
            if 65 <= ordChr <= 88 or 97 <= ordChr <= 120:
                encryptMsg += chr(ordChr + 2)
            elif 48 <= ordChr <= 56:
                encryptMsg += chr(ordChr + 1)
            elif ordChr == 89 or ordChr == 90 or ordChr == 121 or ordChr == 122:
                encryptMsg += chr(ordChr - 24)
            elif ordChr == 57:
                encryptMsg += chr(ordChr - 9)
        print('加密字符串为：', encryptMsg)
    elif options == 2:
        msg = input('请输入待解密字符串：')
        encryptMsg = ''
        for i in msg:
            ordChr = ord(i)
            if 65 <= ordChr <= 88 or 97 <= ordChr <= 120:
                encryptMsg += chr(ordChr - 2)
            elif 48 <= ordChr <= 56:
                encryptMsg += chr(ordChr - 1)
            elif ordChr == 89 or ordChr == 90 or ordChr == 121 or ordChr == 122:
                encryptMsg += chr(ordChr + 24)
            elif ordChr == 57:
                encryptMsg += chr(ordChr + 9)
        print('解密字符串为：', encryptMsg)
    else:
        print('输入错误，请重新输入')
    print()
