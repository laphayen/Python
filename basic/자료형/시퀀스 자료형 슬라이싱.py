
# 시퀀스 자료형 슬라이싱
# 인덱스로 범위를 취함

# [시작 인덱스:끝 인덱스:스텝(1일 경우 생략)]
# [a:b] - a이상 b미만
# [:b] - 처음부터 b미만까지
# [a:] - a부터 끝까지
# [:-b] - 처음부터 (뒤에서 b미만까지) 
# [-a:] - (뒤에서 a부터) 끝까지   

# 0시작, 음수는 반대

s = '12345'
l = [1,2,3,4,5]
t = (1,2,3,(4,5))

print(s[0:2])
print(l[-1:])
print(t[::2])
