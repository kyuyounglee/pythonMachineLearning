class Student:
    def __init__(self,name,kor,eng):
        self.name = name
        self.kor = kor
        self.eng = eng

    def getAvg(self):
        return (self.kor + self.eng) / 2

    def __eq__(self, other):
        return self.getAvg() == other


test = Student("A",90,90)
print(test == 90)