
# for문
# for 변수 in 범위:
#    반복으로 실행할 코드

# for문 범위로 사용되는 것 - 시퀀스 자료형 or 반복 가능한 자료
# 문자열, 리스트나 튜플, 사전, range(), 그 외 반복가능한 개체

scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)


# 문자열 범위
str = 'abc'
for x in str:
    print(x)

# 리스트 범위
nlist = [1, 2, 3]
for x in nlist:
    print(x)

# 사전 범위
ndist = {'a':1, 'b':2, 'c':3}
for x in ndist:
    print(x)

# range() 함수
for x in range(3):
    print()
