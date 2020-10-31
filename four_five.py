import random

matrix = list()
size = int(input('输入矩阵大小（X*X）：'))
print('正在随机生成矩阵中，请稍后...')
for i in range(size):
    rowList = list()
    for j in range(size):
        rowList.append(random.randint(0, 50))
    matrix.append(rowList)
print('矩阵随机生成成功：', matrix)
for i in matrix:
    matrixRowMax = max(i)
    index = i.index(matrixRowMax)
    rowList = list()
    for j in range(matrix.__len__()):
        rowList.append(matrix[j][index])
    rowMinIndex = rowList.index(min(rowList))
    if rowMinIndex != index:
        print('没有鞍点')
    else:
        print('找到鞍点', '位置是：', index)
        break
