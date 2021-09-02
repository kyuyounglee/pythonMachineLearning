class Student:
    def __init__(self, name, kor=0, eng=0, math=0, science=0):
        # instance 변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.science = science

    def sum(self):
        return self.kor+self.math+self.eng+self.science

    def average(self):
        return self.sum() / 4

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.name, self.kor, self.eng,
            self.math, self.science)

    def showTotalAvg(self):
        return "{}\t{}\t{}".format(self.name, self.sum(), self.average())

# 객체생성
student = Student('홍길동')

# 생성된 객체를 리스트로 관리
students = [
    Student('홍길동1', 99, 55, 87, 100),
    Student('홍길동2', 89, 98, 87, 100),
    Student('홍길동3', 89, 98, 67, 98),
    Student('홍길동4', 79, 98, 87, 88),
]

# 학생들의 총점과 평균을 listup
for obj in students:
    print(obj.showTotalAvg())
print("================================")
for obj in students:
    print(str(obj))





