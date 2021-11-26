
# 클래스 맴버 / 인스턴스 맴버
# 클래스 맴버 - 클래스 메소드 바깥 선언
# 인스턴스 맴버 - 클래스 메소드 안에 self와 선언

class c:
    n = 11618
    def p(self):
        param1 = '1234'
        # 클래스 내의 멤버를 참조
        self.param2 = '5678'
        print(param1)
        print(self.n)
        
obj = c()
# 클래스 밖에서 클래스 이름만 참조(사용 빈도 낮음)
print(c.n)
# 클래스의 만든 인스턴스 객체에서 변수를 참조
print(obj.n)
obj.p()

        