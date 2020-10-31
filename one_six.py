import math

radius, high = eval(input('输入圆柱体的半径和高：（逗号隔开）'))
print('圆柱体的表面积为：', str(2 * (math.pi * radius * radius) + (2 * math.pi * radius * high)))
