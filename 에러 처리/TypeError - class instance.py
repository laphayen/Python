
# TypeError: __init__() missing 1 required positional argument: '생성자 인자값'
# 인자를 입력하지 않고 인스턴스 객체를 생성할 경우

class c:
    def __init__(self, s):
        self.var = s
        print('생성자 인자값: '+ s)

# 인자값을 지정하지 않아서 오류가 발생
# obj = c('인자값')
obj = c()
    