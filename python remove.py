
from os import remove

f ='codeomni.txt'
i = input('파일을 삭제합니다 Y/N')
if i == 'Y':
    remove(f)
    print('codeomni.txt 파일이 삭제되었습니다.')
    