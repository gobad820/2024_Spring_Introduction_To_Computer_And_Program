n = int(input('n을 입력하시오 : '))
while n <= 0 or n >= 10:
    n = int(input('n을 입력하시오 : '))

n_list = []

print()
for i in range(n):
    m_list = []
    index = i*n
    if (i % 2) == 0:
        for j in range(index+1,index+n+1,1):
            m_list.append(j)
    else:
        for j in range(index+n,index,-1):
            m_list.append(j)
    n_list.append(m_list)

for m in n_list:
    for j in m:
        print(f'{j:>2}', end='  ')
    print()

