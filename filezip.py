
import zipfile

def compressZip(zipname, filename):
    print('[%s] -> [%s] 압축...' %(filename, zipname))
    with ZipFile(zipname, 'w') as ziph:
        ziph.write(filename)
    
    print('압축 완료')

filename = 'codeomni.txt'
zipname = filename + '.zip'
compressZip(zipname, filename)
