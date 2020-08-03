
# open(파일이름, 모드)
# 텍스트 파일과 바이너리 파일(ex 사진) 읽기

# 텍스트 모드로 읽기: r or rt
f1 = open('text.txt', 'r')

# 텍스트 모드로 읽기: w or wt
f2 = open('text.txt', 'w')

# 텍스트 모드로 파일 마직막에 추가: a or at
f3 = open('text.txt', 'a')

# 바이너리 모드로 읽기: rb
f4 = open('img.jpg', 'rb')

# 바이너리 모드로 읽기: wb
f5 = open('img.jpg', 'wb')

# 바이너리 모드로 파일 마직막에 추가: ab
f6 = open('img.jpg', 'ab')
