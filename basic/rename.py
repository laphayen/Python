
import os

d = input('디렉토리 이름 입력: ')

try:
    os.mkdir(d)
except Exception as e:
    print(e)
    