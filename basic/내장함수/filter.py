
# filter()
# 특정 조건을 만족할 경우만 추출
# filter(추출하는 함수, 반복가능한 자료)

def getPrime(x):
    if x%2 == 0:
        return
    
    for i in range(3, int(x/2), 2):
        if x % i == 0:
            break
    
    else:
        return x

listdata = [1, 2, 3, 4, 5, 6, 7]
ret = filter(getPrime, listdata)
print(list(ret))
