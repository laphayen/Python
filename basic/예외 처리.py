
# 예외 처리
# 예외 상황이 발생했을 때 종료하지 않고 처리
# 예외는 try ~ except 사이

try:
    # 오류가 발생할 지점
    print(num)
    
# 오류가 발생할 경우 실행    
except:
    print('예외처리')
    
# except Exception as e
# 예외 발생 내용을 확인 방법
# 파이썬은 발생 가능한 예외,에 대해 excption 객체로 미리 정의
# http://docs.python.org/3/library/exceptions.html#bltin-exptions

try:
    print(num)
except Exception as e:
    print(e)

num = 1
try:
    while(1):
        print(num)
        num += 1

# 특정 오류가 발생할 경우
except KeyboardInterrupt:
    print('키보드 입력 중단')
