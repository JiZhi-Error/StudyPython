if __name__ == '__main__':
    lose = 0
    grand = 0
    while True:
        score = int(input('请输入考试成绩（输入-1退出程序）：'))
        if 0 <= score <= 100:
            if score >= 90:
                grand += 1
            elif score < 60:
                lose += 1
            print('不及格人数：', lose, '\t90分以上人数：', grand)
        else:
            print('数据非法，退出执行')
            break
