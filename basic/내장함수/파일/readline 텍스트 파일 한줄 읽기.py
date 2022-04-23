
# readline
# 텍스트 파일 읽기

f = open('test.txt', 'r')
line_num = 1
line = f.readline() 
while line:
    print('%d %s' %(line_num, line), end='')
    line= f.readline()
    line_num += 1
f.close()
