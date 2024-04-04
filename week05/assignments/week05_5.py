def get_birthdate(register_number):
    birth_year = 1900 + int(register_number[:2])
    if birth_year % 100 < 50:
        birth_year += 100
    birth_month = int(register_number[2:4])
    birth_day = int(register_number[4:6])
    return birth_year, birth_month, birth_day


resident_register_num = input('주민등록번호 첫 6숫자 형식 입력: ')
birthdate = get_birthdate(resident_register_num)
print(f'{birthdate[0]}년 {birthdate[1]}월 {birthdate[2]}일')
