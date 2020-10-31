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
    del matrixRow

# 这部分代码可以在后续运行中删除，只是为了检测计算结果是否正确mei
# 循环显示出矩阵内数据
for i in matrixList:
    for j in i:
        print(j, end='\t')
    print()

maxRowList = list()
minRowList = list()
for i in matrixList:
    maxRowList.append(max(i))
    minRowList.append(min(i))
# 获取到最大值以及最小值
max1 = max(maxRowList)
min1 = min(minRowList)
del maxRowList
del minRowList
maxIndexList = list()
minIndexList = list()
for index, i in enumerate(matrixList):
    # 这是最大数
    if max1 in i:  # 先判断该行有没有这个数
        numIndex = 0
        count = i.count(max1)
        for j in range(count):
            maxIndexList.append('(%d,%d)' % (index, i.index(max1, numIndex)))
            numIndex = i.index(max1, numIndex) + 1

    # 这是最小数
    if min1 in i:  # 先判断该行有没有这个数
        numIndex = 0
        count = i.count(min1)
        for j in range(count):
            minIndexList.append('(%d,%d)' % (index, i.index(min1, numIndex)))
            numIndex = i.index(min1, numIndex) + 1
print('最大值坐标集合为：', maxIndexList)
print('最小值坐标集合为：', minIndexList)
print('最大值为：', max1)
print('最小值为：', min1)
