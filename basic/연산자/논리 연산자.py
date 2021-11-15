# 논리 연산자


# and - 피연산자 두개가 모두 참일 때 True 출력, 나머지 경우 모두 False 출력
num_one = 7
num_two = 9
print(num_one < 8 and num_two > 6)
print(num_one < 7 and num_two > 5)
print(num_one != 7 and num_two !=9)

# or - 하나만이라도 참일 경우 True(1) 출력
n1 = 1
n2 = 0
print(n1 or n1)
print(n1 or n2)
print(n2 or n2)

# not Bool을 반대로 전환

print(not True)
print(not False)
