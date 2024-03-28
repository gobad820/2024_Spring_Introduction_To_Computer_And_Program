## 삽입정렬
input_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
### driven code; i번째 칸을 정렬하라. 큰 의미는 X
for i in range(1, len(input_list)):
    for j in range(i,0,-1):
        if input_list[j] > input_list[j -1]:
            input_list[j], input_list[j - 1] = input_list[j - 1],input_list[j]

print(input_list)
