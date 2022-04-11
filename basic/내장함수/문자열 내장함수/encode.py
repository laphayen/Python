
# encode
# 문자열을 2진 스트림 데이터인 바이트 객체로 변환

utxt = '11618nathan'
btxt = utxt.encode()

print(utxt)
print(btxt)

ret1 = '1' == utxt[0]
ret2 = '1' == btxt[0]
print(ret1)
print(ret2)
