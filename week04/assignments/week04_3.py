input_num = 0

while input_num < 1 or input_num > 10:
    input_num = int(input('숫자를 입력하세요: '))

matrix_list = []
for i in range(1, input_num * input_num + 1):
    matrix_list.append(i)

for i in range(input_num):
    if i % 2 == 0:
        for j in matrix_list[input_num*i:input_num*(i+1)]:
            print(f"{j:4d}",end="")
    else:
        reversed_matrix_list = matrix_list[input_num*i:input_num*(i+1)]
        reversed_matrix_list.reverse()
        for j in reversed_matrix_list:
            print(f"{j:4d}",end="")
    print()
