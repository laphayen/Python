
# 클래스 상속
# 부모클래스의 모든 기능들을 자식클래스로 상속
# 부모클래스, 슈퍼클래스 - 상속해주는 클래스
# 자식클래스, 서브클래스 - 상속 받는 클래스

# class 자식클래스(부모클래스):
# 부모와 자식의 동일 이름이 멤버, 메소드일 경우 자식클래스에서 정의 우선

# 다중 상속 - 여러 부모클래스에게 상속 받음.
# class 자식클래스(부모클래스1, 부모클래스2, ...)

class add():
    def addnum(self, n1, n2):
        return n1 + n2

class sub():
    def subnum(self, n1, n2):
        return n1 - n2

# 다중 상속
class cal(add, sub):
    def mulnum(self, n1, n2):
        return n1 *  n2

obj = cal()
print(obj.addnum(16, 8))
print(obj.subnum(16, 8))
