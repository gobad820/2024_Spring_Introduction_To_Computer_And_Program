height = 0
day = 0
while height < 30:
    day += 1
    height += 7
    print(f'day : {day}  달팽이의 위치 : {height} 미터')
    if height >= 30:
        break
    height -= 5
print(f'\n우물을 탈출하는 데 걸린 날을 {day}일 입니다.', end='')
