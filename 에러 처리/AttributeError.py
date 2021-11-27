
# AttributeError
# AttributeError: 'c' object has no attribute '변수명'
# 클래스 매소드를 호출 전에 매소드 내에 선언된 인스턴스 멤버를 호출할 경우 발생
# 클래스 매소드의 지역변수를 참조할 경우 발생

class c:
    def cm(self):
        n = 11618
        self.param = '1234'

obj = c()

# 오류 발생
# print(obj.param)

obj.cm()
print(obj.param)

# 오류 발생
# print(obj.n)
