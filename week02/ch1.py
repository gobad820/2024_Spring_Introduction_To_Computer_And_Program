chicken = 2
pig = 3
cow = 4

chicken_leg = 2
pig_leg = 4
cow_leg = 4

print('전체 다리의 수: '+str(chicken_leg*chicken + pig*pig_leg+cow*cow_leg))

hour = int(input('시간을 입력하시오: '))
minutes = int(input('분을 입력하시오: '))
print(str(hour)+'시간 '+str(minutes)+' 분은 '+ str(minutes * 60 + hour * 3600)+'초 입니다.')


fahrenheit = int(input('화씨 온도를 입력하시오: '))
celsius = round((fahrenheit - 32.0)*5/9,2)
print('화씨 '+str(fahrenheit)+'도는 섭씨 '+str(celsius)+'도에 해당합니다.')

import turtle
side = 100
turtle.shape('turtle')
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.forward(side)
turtle.left(120)
turtle.done()
