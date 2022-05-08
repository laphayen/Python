
# chr
# 코드값에 해당하는 문자를 반환

print('codeomni')

# 변수에 문자를 입력
val = input('문자 : ')

# 자료형 변환
val = int(val)

try:
    #chr() 함수 사용
    c = chr(val)
    print('코드값: %d, 문자: %s' %(val, c))
except ValueError:
    print('입력 오류')
