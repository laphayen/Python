
# shuffle
# 리스트 요소 무작위 

# random 모듈
from random import shuffle

l = list(range(1, 11))
print(l)

for i in range(3):
    shuffle(l)
    print(l)
    