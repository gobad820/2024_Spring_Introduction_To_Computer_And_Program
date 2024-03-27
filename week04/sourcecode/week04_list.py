# for A in B, B는 무조건 iterable할 수 있어야 한다.
# => 원소를 한 번에 하나씩 꺼낼 수 있어야 한다.
# 따라서 A는 Iterator이며, B는 Iterable하다고 할 수 있다.
# B는 CS에서 자료구조라고 한다. 자료구조를 언어마다 컬렉션을 통해 제공해준다.


# 리스트 ≒ 배열
#   1. 자료구조(반복가능)
#   2. 인덱스

list1 = list()
list2 = []
list3 = list((1,2,3))
list4 = list(range(1,10))
list5 = list('ABCDEF')

# 대괄호가 리스트임을 나타낸다.
n_list = [11,12,13,14,15]
# [index] => 양수 or 음수
print(n_list[-1]) # result : [11, 12, 13, 14, 15]




