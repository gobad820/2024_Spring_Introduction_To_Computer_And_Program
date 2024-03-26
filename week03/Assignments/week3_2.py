x = int(input('x 좌표 : '))
y = int(input('y 좌표 : '))
while x == 0 or y == 0:
    x = int(input('x 좌표 : '))
    y = int(input('y 좌표 : '))

if x > 0 and y > 0:
    print(f'1 사분면 위에 있습니다.')
elif x < 0 and y > 0:
    print(f'2 사분면 위에 있습니다.')
elif x < 0 and y < 0:
    print(f'3 사분면 위에 있습니다.')
else:
    print(f'4 사분면 위에 있습니다.')
