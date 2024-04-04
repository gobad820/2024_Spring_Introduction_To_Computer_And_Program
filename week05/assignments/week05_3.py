def sort_list(number_list):
    sorting_list = number_list
    for i in range(len(sorting_list)-1):
        index = i
        for j in range(i+1,len(sorting_list)):
            if sorting_list[j] < sorting_list[index]:
                index = j
        sorting_list[i],sorting_list[index] = sorting_list[index],sorting_list[i]
    return sorting_list


# 입력
str_numbers = input('쉼표로 구분된 정수를 여러 개 입력하시오: ').split(',')

# 정수로 변경
int_numbers = [int(i) for i in str_numbers]

# 정렬
sorted_list = sort_list(int_numbers)

# 출력
print(f'입력된 정수의 리스트: {int_numbers}')
print(f'정렬된 정수의 리스트: ', end='')
for i in sorted_list:
    print(i, end=' ')
