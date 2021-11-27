
# 클래스 메소드
# 클래스 내에서 정의되는 함수
# 첫 번째 인자는 self
# self - 해당 클래스의 인스턴스 객체를 지시하는 참조자, 인자를 넘겨줄 경우 두 번째 인자부터 정의

class c:
    def s1(self):
        print("문자열")
    
    def p2(self, num):
        print("숫자:  %d" %num)

obj = c()
obj.s1()
obj.p2(11618)
