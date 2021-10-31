# if
# 조건문 조건에 따라 코드를 실행

num = input("숫자 입력: ")
num = int(num)

# 조건을 검사
if num > 0:
    # 참일 경우
    print("양수입니다.")

# if가 아니고 elif 조건이 참일 경우만 실행
elif  num < 0:
    print("음수입니다.")

# 위의 조건이 모두 아닐 경우 실행
else :
    print("0입니다.")


# 조건을 참일 경우만 로직 구현 -> else문 사용X
if num > 0:
    print("0보다 큽니다.")