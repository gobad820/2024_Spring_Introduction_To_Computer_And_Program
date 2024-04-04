from math import pi

def input_radius():
    radius = int(input('반지름을 입력하시오: '))
    return radius

def area_and_circumference(r):
    circumference = 2 * pi * r
    area = pi * (r ** 2)
    return area, circumference

radius = 0
while radius >= 0:
    radius = input_radius()
    if radius < 0:
        break
    area, circumference = area_and_circumference(radius)
    print(f'넓이 :{area:7.3f}, 둘레 :{circumference:7.3f}')
print('프로그램을 종료합니다.')
