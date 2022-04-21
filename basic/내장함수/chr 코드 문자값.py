
# chr
# 코드값에 해당하는 문자를 반환

val = input('문자 : ')
val = int(val)
try:
    c = chr(val)
    print('코드값: %d, 문자: %s' %(val, c))
except ValueError:
    print('입력 오류')
