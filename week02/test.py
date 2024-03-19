# 변수는 메모리 주소의 alias, 그래서 자료형은 ?
# 그래서 자료형은 ? 숫자는 사칙 연산에 닫혀있고 문자는 사칙 연산에 닫혀있지 않다.

import math

print('100과 200의 평균',(100+200)/2)
"""
반지름을 사용해서 면적과 둘레를 계산하는 코드입니다.
"""
radius = 15.23

PI = 3.14 # 상수는 대문자로 취급한다.

# 변수명이 숫자로 시작하면 안된다.

# 출력문 <-- 주석문
print('원의 반지름', radius)

# 원의 넓이를 출력 <-- 주석문
print('원의 면적',  math.pi * radius * radius)

# 원의 둘레를 출력 <-- 주석문
print('원의 둘레', 2.0 *  PI * radius)


width = 10
height = 5
width = 20 # 변수 재할당 # 변수 값을 다른 값으로 바인딩한다.
rectangle_area = width * height
print('사각형의 면적 :', rectangle_area)


# 변수명은 띄어쓰면 안된다.
# student name = '홍길동' X
student_name = '홍길동'

"""
정적
    => 사전에 계산 되어져 스택에 올라가 있음
    => 검증 가능하다.

동적
    => 현재 시점에 계산 중
    => 검증이 힘들다.


변수를 보명 자료형을 생각하여서 연산을 고려하며 코딩한다.
"""

l = [100,300,500,900]
print(type(l))
# orthogonality 하지 않다 => 같은 일을 하는 함수가 2개

txt5 = 'banana\napple\norange'
print(txt5) # 출력 결과는?

txt6 = 'banana\tapple\torange'
print(txt6)


# 동시 할당문
num4, num5 = 200, 300
print(num4,num5)

# not 연산자는 일항연산자이다.
x, y = True, False
print(not y)

# 비트 연산자는 안 온다.

width = input()
height = input()
print(width,height)

