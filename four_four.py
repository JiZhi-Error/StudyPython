scoreList = list()
while True:
    score = int(input('输入成绩（输入-1退出输入）：'))
    if score == -1:
        break
    scoreList.append(score)
scoreSum = sum(scoreList)
averageValue = scoreSum // (scoreList.__len__())
num = 0
for i in scoreList:
    if i >= averageValue:
        num += 1
print('平均值为：', averageValue)
print('高于和等于平均值人数为：', num)
print('成绩集合为：', scoreList)
