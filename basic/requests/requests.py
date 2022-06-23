
import requests

x = requests.get('https://github.com/laphayen')

print(x.text)
