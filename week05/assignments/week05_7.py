def unit_fraction(frac):
    unit_frac = 1
    while unit_frac > frac:
        prev = unit_frac
        unit_frac = 1 / (1 / unit_frac + 1)

    if abs(unit_frac - frac) > abs(prev - frac):
        unit_frac = prev

    return 1 / unit_frac


frac = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
unit_frac = unit_fraction(frac)
print(f'가장 가까운 단위 분수는 1/{unit_frac:.0f}이며, 이 값은 {1 / unit_frac}입니다.')
