# 갸위/바위/보
me = "가위"
you = "보"
if me == you:
    print('무승부')
elif me == "가위":
    if you == "보":
        print('승리')
    elif you == "바위":
        print('패배')
elif me == "바위":
    if you == "보":
        print('패배')
    else:
        print("승리")
else:  # "보"
    if you == "바위":
        print('승리')
    else:
        print("패배")

for i in range(5):
    print(f"{i} : Hello, World")

for _ in range(5):
    print(f"Hello, World")

# 1 ~ N까지 덧셈 단, (n*(n+1))/2 금지

# 애초에 range에서 필터링을 할 수 있으면 필터링해서 넣는다
# 안되면 if문으로 실시간으로
N = 10
result = 0
for i in range(0, N + 1):  # for는 반복문 keyword, in은 범위를 나타내는 keyword
    if i != 4:
        result += i
print(f"결과는 {result}")

r = "a" in "apple"
print(r)

# List Comprihension

# 중첩 반복문 => 대부분의 문제는 선형으로 만들면 풀 수가 있다
# => 선형은 행렬로 표현할 수 있다
# => 행렬은 중첩 반복문으로 할 수 있다.

# 알고리즘에서 O(N^2) => O(N)으로 바꾸면 무조건 시험 오호


N = 10
result = 0
for i in range(1, N, 3):
    for j in range(1,N):
        print(f'{i} * {j} = {i * j}', end='\t')
        print(f'{i + 1} * {j} = {(i + 1) * j}', end='\t')
        print(f'{i + 2} * {j} = {(i + 2) * j}')
# 55번 블록이 끝나야 i가 증가한다. 모든 프로그램은 순차적으로
