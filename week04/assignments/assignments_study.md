# 과제에서 배운 개념

## .reverse() vs reversed(obj)
두 함수 모두 리스트를 반전시키는 역할을 한다. 하지만 .reverse() 함수는 앞에 나온 함수 자체를 반전시키기 때문에 리턴값이 따로없다. 하지만 reversed()함수의 경우 새로운 리스트를 리턴값으로 주기 때문에 새로운 리스트에 할당시켜주어야 사용이 가능하다.

```python
list = [1,2,3]
reversed_list = reversed(list)
print(list)             # [1, 2, 3]
print(reversed_list)    # [3, 2, 1]
```
```python
list = [1, 2, 3]
list.reverse()
print(list)  # [3, 2, 1]

```
### 슬라이싱과 반전 같이 쓰기
**슬라이싱의 경우 expression이 아닌 assignment이다.** 따라서 슬라이싱을 통해 새로운 변수에 리스트를 넣어준 후에 반전을 시켜야 원하는 값을 얻을 수 있다.


## isalpha
isalpha 함수는 매개변수로 들어온 값이 알파벳으로 이루어진 값인지 확인하는 함수이다.
```python
def isalpha(self, *args, **kwargs): # real signature unknown
    """
    Return True if the string is an alphabetic string, False otherwise.
    
    A string is alphabetic if all characters in the string are alphabetic and there
    is at least one character in the string.
    """
```

## isnumeric
isnumeric 함수는 매개변수로 들어온 문자열이 숫자로 이루어진 문자열일 때 True를 Return하고 그렇지 않으면 False를 Return한다.
```python
def isnumeric(self, *args, **kwargs): # real signature unknown
    """
    Return True if the string is a numeric string, False otherwise.
    
    A string is numeric if all characters in the string are numeric and there is at
    least one character in the string.
    """
```


## 오답풀이

과제 1번의 경우 각각의 케이스를 나누어서 케이스마다 풀도록 하여야 한다. 통으로 문제를 접근하려는 방식은 좋은 것이 아니다.
문제를풀 때 크게 3가지 부분ㄹ으로 나누면 좋다. Input, Process, Output으로 삼분할 풀 수 있다.

### 문제4-3

```python
# list assignment
alist = list(range(1,input**2+1))

```
list.extend함수 복습 필요