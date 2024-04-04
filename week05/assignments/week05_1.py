# 섭씨온도를 화씨온도로 변환
def cel2fah(cel):
    fahrenheit = (cel * 1.8) + 32
    return fahrenheit


start_temp = 10
end_temp = 51
step = 10
degree_sign = u'\N{DEGREE SIGN}'
for i in range(start_temp, end_temp, step):
    print(f'섭씨온도 {i}{degree_sign}C = 화씨온도 {cel2fah(i):5}{degree_sign}F')
