import random

# 以下部分是随机生成矩阵
matrixList = list()
matrixListSize = int(input('请输入随机矩阵大小(X*X)：'))  # 矩阵的宽高一致
# 两层for循环进行随机填充数据，随机填充数据采用“random”函数随机生成
for i in range(matrixListSize):
    matrixRow = list()  # 矩阵的一列数据
    for j in range(matrixListSize):
        matrixRow.append(random.randint(0, 100))  # 采用0到100随机
    # 将生成好的一列数据添加到矩阵总集合中
    matrixList.append(matrixRow)

# 这部分代码可以在后续运行中删除，只是为了检测计算结果是否正确mei
# 循环显示出矩阵内数据
for i in matrixList:
    for j in i:
        print(j, end='\t')
    print()

diagonal = 0  # 对角线
obliqueDiagonal = 0  # 斜对角线
# 此处计算一个循环足以，上次弄麻烦了
for i in range(matrixList.__len__()):
    diagonal += matrixList[i][i]
    obliqueDiagonal += matrixList[matrixList.__len__() - 1 - i][i]

print('对角线之和为：', diagonal)
print('斜对角线之和为：', obliqueDiagonal)
