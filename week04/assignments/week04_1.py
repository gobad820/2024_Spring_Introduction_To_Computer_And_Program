src = input('문자열을 입력하세요: ')
while not src.isalpha():
    src = input('문자열을 입력하세요: ')
zipped_list = []
temp_character = src[0]
count = 0
for i in src:
    if temp_character == i:
        count += 1
    else:
        zipped_list += temp_character + str(count)
        count = 1
        temp_character = i
zipped_list += temp_character + str(count)

for i in zipped_list:
    print(i,end="")