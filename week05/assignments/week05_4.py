def fibo(num):
    fibo_list = []
    for i in range(num + 1):
        if i <= 1:
            fibo_list.append(1)
        else:
            fibo_num = fibo_list[i - 2] + fibo_list[i - 1]
            fibo_list.append(fibo_num)
    return fibo_list


iteration = 15
number = 15

fibonacci_list = fibo(number)

for i in range(len(fibonacci_list)):
    print(f'fibo({i:3d}) = {fibonacci_list[i]:8d}')
