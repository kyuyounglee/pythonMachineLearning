class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        print("Person 초기화 호출")
    def work(self):
        print("work")


class Student(Person):
    def __init__(self, a, b, c, tname):
        Person.__init__(self, a, b, c)
        self.tname = tname
        print("Student 생성자 호출")
    def study(self):
        print("study")


class Teacher(Person):
    def teach(self):
        print("teach")


st = Student('홍길동', 100, '동해번쩍서해번쩍', '홍선생')
print(st.name)
print(st.tname)
# te = Teacher()
# st.study()
# st.work()
# te.teach()
# te.work()
