
# urlopen
# url을 사용해서 웹페이지 html을 화면에 출력

from urllib.request import urlopen
url = 'https://www.python.org'

with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)
    