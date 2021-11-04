
# 반복문

# 특정 조건을 만족하는 경우 지속적으로 반복을 수행

# while 조건:
#   반복 실행 코드
#   continue - 구문 처음으로 이동 후 반복
#   break - while문 탈출

num = 1

while num < 5:
    print(num)
    num = num + 1
    if num < 3:
        continue
    else:
        break

