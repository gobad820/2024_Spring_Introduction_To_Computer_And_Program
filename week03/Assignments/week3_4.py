prime_number = int(input('숫자를 입력하세요 : '))
if prime_number == 1:
    print(f'{prime_number}는 소수가 아닙니다')
else:
    for i in range(2, prime_number + 1):
        if i == prime_number:
            print(f'{prime_number}는 소수입니다.')
            break
        if prime_number % i == 0:
            print(f'{prime_number}는 소수가 아닙니다')
            break
