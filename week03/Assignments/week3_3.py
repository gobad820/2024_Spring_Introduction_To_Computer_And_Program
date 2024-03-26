number = int(input('1에서 9까지의 수를 입력하세요: '))
while number <= 0 or number > 9:
    number = int(input('1에서 9까지의 수를 다시 입력하세요: '))
for j in range(1, 10, 1):
    print(f'{number} x {j} = {number * j}')
