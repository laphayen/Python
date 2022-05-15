
# remove
# 파일 삭제하기
# os 모듈의 remove() 사용

from os import remove

target_file = 'test.txt'

c = input('파일 삭제(y/n)')
if c == 'y':
    remove(target_file)
    print('codeomni')
    print('파일 삭제 완료')
