numbers = []

for i in range(3):
    number = int(input(f'{i + 1}번째 수를 입력하세요: '))
    if i == 0:
        numbers.append(number)
    else:
        for j in range(i):
            if numbers[j] > number:
                numbers.insert(j, number)
                break
            if j == i - 1:
                numbers.append(number)

print(numbers)
