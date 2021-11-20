
# TypeError tuple
# 튜플은 요소의 값을 변경X
# ypeError: 'tuple' object does not support item assignment

t = (1, 2, 3, 4, 5)
print(t)

# 튜플 값 변경 -> 오류
t[3] = 0
print(t)
