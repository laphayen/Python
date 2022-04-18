
# enumerate
# 리스트 요소를 인덱스와 쌍으로 추출

l = ['n', 'a', 't', 'h', 'a', 'n']
r = list(enumerate(l))
print(l)

for i, body in enumerate(l):
    print('%d: %s' %(i, body))
    