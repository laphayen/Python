
from urllib.request import urlopen

bursize = 256*1024

fileurl = 'https://blog.kakaocdn.net/dn/c2BsVq/btqFFTNlDTN/wFsgLX63BFyVymkC0GTmzk/img.png'
filename = fileurl.split('/')[-1]

try: 
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(bursize)
            while buf:
                h.white(buf)
                buf = f.read(bursize)

except Exception as e:
    print(e)
