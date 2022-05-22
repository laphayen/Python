
# url 쿼리 분리

url = 'http://11618nathan.github.io/python'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)
