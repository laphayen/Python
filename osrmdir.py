
import os

f ='codeomni'
i = input('codeomni 디렉토리를 삭제합니다 Y/N')
if i == 'Y':
    os.rmdir(f)
    print('codeomni 디렉토리가 삭제되었습니다.')
    