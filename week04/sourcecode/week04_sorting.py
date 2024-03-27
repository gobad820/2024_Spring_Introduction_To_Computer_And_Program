# 정렬 3종 세트 # 시험문제 X
# 코테에서 nlogn으로 개선시키는 문제를 위해서 꼭 알아두어야 한다.
## 선택정렬

input_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(input_list)):
    # TODO 1. 주어진 리스트 중에 최소값을 찾는다.
    min_index = i
    for j in range(i + 1, len(input_list)):
        if input_list[j] < input_list[min_index]:
            min_index = j
    # TODO 2. 그 값을 맨 앞에 위치한 값과 교체한다.
    input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    # TODO 3. 맨 앞의 값을 뺀 나머지 값에 대해서 반복한다.
print(input_list)
