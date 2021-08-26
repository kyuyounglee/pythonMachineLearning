# 시험 과목이 국 영 수
# 합격의 조건이   평균 60점이상 이고 각 과목의 점수가 40점 이상
kor = int(input("국어점수:"))
eng = int(input("영어점수:"))
math = int(input("수학점수:"))
print(
    (kor+eng+math) / 3 >= 60
    & kor >= 40
    & eng >= 40
    & math >= 40
)
isPass = (kor+eng+math) / 3 >= 60 & kor >= 40 & eng >= 40 & math >= 40
if isPass:
    print("합격")
else:
    print("불합격")

#삼항연산자
print("합격" if isPass else "불합격")

