scoreList = list()
while True:
    score = int(input('请输入成绩(输入“-1”结束输入)：'))
    if score == -1:
        break
    if 0 <= score <= 100:
        scoreList.append(score)
    else:
        print('数据不符合规定，请重新输入')
# 输出下当前集合中的所有数据
print('所有成绩为：', scoreList)
scoreAverage = sum(scoreList) // scoreList.__len__()  # 计算平均数
# 再循环找到高于和等于平均成绩的人
sum = 0
for i in scoreList:
    if i <= scoreAverage:
        sum += 1
print('高于和等于平均成绩的人数为：', sum, '人')
