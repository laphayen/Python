
from urllib.request import urlopen

imgurl = 'https://11618nathan.github.io/'
imgname = imgurl.split('/')[-1]

try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)
