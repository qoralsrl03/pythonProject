# 클래스
# python도 객체지향 프로그래밍(OOP)
# 클래스 명은 capwords 방식으로 표기
# 함수, 변수, 속성 - 스네이크 표기법 abc-def
# 클래스, 예외는 - 파스칼 표기법 : 첫 문자 대문자.

class Rectangle:
    count = 0 #클래스 변수
    #initalizer
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 1. 인스턴스 메서드(default)
    def calcArea(self):
        area=self.width * self.height
        return area

    # 2. 정적 메서드 self 접근할 수 없음
    @staticmethod
    def isSquare():
        print('정적 메서드')

    # 3. 클래스 메서드 self대신 cls접근
    @classmethod
    def printCount(cls):
        print('클래스 메서드')
        print(cls.count)

    # 연산자 오버로딩
    # 객체끼리의 더하기를 수행할때 실행됨
    def __add__(self,other):
        obj = Rectangle(self.width + other.width
                        ,self.height + other.height)
        return obj
    # 객체끼리의 빼기 수행시에도 자동 실행됨
    def __sub__(self,other):
        obj = Rectangle(self.width - other.width
                        ,self.height - other.height)
        return obj

#인스턴스화 a
a=Rectangle(5,10)
print(a.calcArea())
#인스턴스화 하지 않고 메소드 호출
Rectangle.isSquare()
Rectangle.printCount()
b=Rectangle(10,10)
c=a+b # 객체 + 하게되면 __add__ 라는 함수를 자동으로 호출함.
print(c.width)
d=a-b
print(d.width)
