# TODO sum a, b
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
