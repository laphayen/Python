
from os import rename

f ='codeomni.txt'
i = input('파일을 이름을 변경합니다 Y/N')
if i == 'Y':
    j == input('변경할 이름 입력: ')
    rename(j, f)
    print(f)
    