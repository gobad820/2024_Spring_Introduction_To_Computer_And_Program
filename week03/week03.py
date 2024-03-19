#제어문 => 흐름 제어
# 1. 조건문
# 2. 반복문

# if-elif-else문


age = 20
if age < 20:
    print('청소년 할인')
else:
    print('청소년 할인이 안 됨')

# elif문
score = int(input('점수를 입력하세요 : '))
grade = ''
if score >= 95:
    grade = 'A+'
elif score >= 90:
    grade = 'A'
elif score >= 85:
    grade = 'B+'
elif score >= 80:
    grade = 'B'
elif score >= 75:
    grade = 'C+'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'당신의 점수는 {score}, 당신의 학점은 {grade} 입니다.')
