num = int(input('정수를 입력하시오 : '))
str_num = str(num)
str_num_front = ""
str_num_rear = ""
if len(str_num) % 2 == 0:
    for i in range(0, len(str_num) // 2):
        str_num_front += str_num[i]
    for i in range(len(str_num) // 2, len(str_num)):
        str_num_rear += str_num[i]
else:
    for i in range(0, len(str_num) // 2):
        str_num_front += str_num[i]
    for i in range(len(str_num) // 2 + 1, len(str_num)):
        str_num_rear += str_num[i]

if str_num_rear[::-1] == str_num_front:
    print(f'{num}은(는) 거꾸로 정수입니다.')
else:
    print(f'{num}은(는) 거꾸로 정수가 아닙니다.')
