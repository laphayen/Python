
# del
# 리스트 제거
# 리스트 특정 위치 요소 제거


l = ['n', 'a', 't', 'h', 'a', 'n']

del l[1]
print(l)

# 슬라이싱 - 특정 구간 제거
del l[0:2]
print(l)

# 리스트 자체를 메모리 제거
del l
print(l)
