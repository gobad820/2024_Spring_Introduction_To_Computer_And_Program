def sum1():
    a = 5
    b = 5
    print(f"{a}+{b}={a + b}")


# 함수의 구성요소 정의부, 이름, 매개변수, 본문, 반환값
def sum2():  # def: 함수정의부 sum2: 함수이름 (): 매개변수
    # 본문
    a = 5
    b = 5
    # 반환값
    return a + b  # return없는 함수는 당분간 생성하지 않는다.


sum1()  # 함수호출
print(f"{5}+{5}={sum2()}")  # 결과값을 return받아서 쓸 수 있게 한다.

x = 5
y = 10 # non-local variable

# Comment 함수를 만들 때 지역변수를 사용하라
def sum(x, y):  # 함수 정의, 매개변수는 함수를 정의할 때 사용한다.
    x = 1.0 # scope : 변수가 statement 넘어로 visible한 범위
    y = 2.0 # 지역변수 (local variable)
    return x + y
# 지역에서 바깥에 있는 변수 -> 전역변수, 어디서든 호출이 가능하다.

result = sum(x, y)  # 인자(argument)는 함수를 호출할 때 사용한다.
# 인자를 sum 함수 호출할때에 전달한다.
print(f"{x} + {y} = {result}")
# sum(x, y)를 호출할 때 x, y라는 인자(argument)를 갖고 호출한다.

# 위치 매개면수
def newsum(x=1,y=1):
    return x,y
result = newsum(2) # 하나라도 넣으면 위치에 맞게 전달해준다.
print(result)