prime_number = int(input('숫자를 입력하세요 : '))
if prime_number == 1:
    print(f'{prime_number}는 소수가 아닙니다')
elif prime_number == 2:
    print(f'{prime_number}는 소수입니다')
else:
    for i in range(2, prime_number):
        if prime_number % i == 0:
            print(f'{prime_number}는 소수가 아닙니다')
            break
        if i == prime_number - 1:
            print(f'{prime_number}는 소수입니다')
