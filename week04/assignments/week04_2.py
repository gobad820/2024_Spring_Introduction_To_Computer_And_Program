zipped_string = input("압축된 문자열을 입력하세요: ")
original_string = []
character = ''
for i in zipped_string:
    if i.isalpha():
        character = i
    if i.isnumeric():
        for j in range(int(i)):
            original_string += character

for i in original_string:
    print(i,end="")


