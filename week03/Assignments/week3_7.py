amstrong_number = []
print(f'세 자리의 암스트롱 수 : ', end="")
for i in range(100, 1000):
    str_number = str(i)
    int_number = 0
    for j in str_number: # for 뒤에 오는 것들은 iterable한 것들이다.
        int_number += int(j) ** 3
    if int_number == i:
        print(int_number, end=" ")
        amstrong_number.append(int_number)
