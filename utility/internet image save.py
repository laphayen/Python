
from urllib.request import urlopen

imgurl = 'https://blog.kakaocdn.net/dn/c2BsVq/btqFFTNlDTN/wFsgLX63BFyVymkC0GTmzk/img.png'
imgname = imgurl.split('/')[-1]

try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)
