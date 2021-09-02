# 부모클래스
class Person:
    def __init__(self, name):
        self.name = name
        print("Person 생성자 호출")

    def PMethod(self):
        print("PMethod", self.name)

# Person 클래스를 상속받아서 새로운 클래스를 만듦
class Student(Person):
    def __init__(self):
        pass
    pass

st =  Student()
st.PMethod()


# 부모에서 상속받은 자식 클래스는
# 1 서로 생성자를 재 정의 안하면 자식객체를 만드는데 제약사항이 없다
# 2 부모의 생성자가 매개변수를 가지는 생성자이고 자식이 생성자를 재 정의 안하면
# 자식의 객체를 만들때  부모의 기본생성자를 호출하기때문에. 에러 발생

# 3 자식클래스에서 생성자를 만들고 그 생성자에서 부모의 생성자를 호출 안하면
# 자동으로 호출되지 않으므로 부모의 instance 변수는 사용 못한다
# 그러나 부모의 함수는 사용 가능
