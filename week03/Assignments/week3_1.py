a, b, c = input(f'세 정수를 입력하세요: ').split()
a, b, c = int(a),int(b),int(c)

if a > b and a > c and b > c:
    print(c,a,b)
elif a > b and a > c and b <= c:
    print(b,c,a)
elif b > a and b > c and a > c:
    print(c,a,b)
elif b > a and b > c and c <= a:
    print(a,c,b)
elif c > a and c > b and a > b:
    print(b,a,c)
else:
    print(a,b,c)


