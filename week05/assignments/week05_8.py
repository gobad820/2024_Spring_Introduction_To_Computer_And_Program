def factorial(k):
    facto = 1
    for i in range(1, k + 1):
        facto *= i
    return facto


def euler(n):
    euler_num = 0
    for i in range(n + 1):
        euler_num += (1 / factorial(i))
    return euler_num


num_list = [5,20]
for i in num_list:
    print(f'euler({i:2d}) = {euler(i):.5f}')
