
# 클래스 생성자
# 클래스 인스턴스 객체가 생성될 때 자동 호출되는 메소드
# 클래스의 인스턴스 멤버를 선언, 초기화와 관련된 작업을 처리
# def__init__(self, *args)

class c1:
    def __init__(self):
        self.s='python'
        print('인스턴스 객체 생성')

class c2:
    def __init__(self, txt):
        self.s = txt
        print('생성자 인자 값: '+self.s )
        


# 생성자의 인자가 없고 생성자 안에서 인스턴스 멤버를 초기화        
obj1 = c1()
print(obj1.s)

# 생성자의 인자가 있을 경우
obj2 = c2('문자열')
 