
# rename
# 파일 이름 변경하기
# os 모듈의 rename() 사용

from os import rename

target_file = 'test.txt'

newname = input('새 파일 이름 입력:')

rename(target_file, newname)

print('codeomni')
print(newname)
