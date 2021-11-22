
# 함수 - def의로 정의
# 독립적 호출
# 함수 생성

def count(number):
    n = 1
    while n <= number:
        print(n)
        n = n + 1

# 리턴값O 인자O
def name1(n1):
    #코드
    return 1

# 리턴값O 인자X
def name2():
    # 코드
    return 2

# 리턴X 인자X
def name3():
    # 코드
    return

# 인자O 리턴O 호출
n1 = name1(1)

# 리턴X
name3() 

# 인자X 리턴X
name3()
