start_number = 1
end_number = 10001
for num in range(start_number,end_number):
    sum_divisor_number = 0
    divisor_number = []
    for i in range(1,num):
        if num % i == 0:
            divisor_number.append(i)
    sum_divisor_number = sum(divisor_number)
    if sum_divisor_number == num:
        print(f'{num}은 완전수입니다')
        print(f'{num}의 약수 : {divisor_number}, 약수의 합 = {sum_divisor_number}')
