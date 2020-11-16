import math

if __name__ == '__main__':
    radius, high = eval(input('请输入圆柱体的半径和高，用“,”隔开：'))
    round_surface_area = math.pi * radius * radius
    round_perimeter = 2 * math.pi * radius
    print('圆柱体表面积为：{}'.format((round_surface_area * 2) + (round_perimeter * high)))
