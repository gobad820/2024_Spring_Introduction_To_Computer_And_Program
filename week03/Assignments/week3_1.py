numbers = []

for i in range(3):
    if i == 0:
        number = int(input('1에서 9까지의 수를 입력하세요: '))
        numbers.append(number)
    else:
        number = int(input('1에서 9까지의 수를 다시 입력하세요: '))
        for j in range(i):
            if numbers[j] > number:
                numbers.insert(j, number)
                break
        if len(numbers) <= i:
            numbers.append(number)

print(numbers)
