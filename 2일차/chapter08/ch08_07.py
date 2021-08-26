import turtle
t = turtle.Turtle()
t.shape("turtle")

scores = [90, 70, 80]

t.forward(200)       # x축 그리기

t.up()
t.goto(0, 0)
t.down()

t.left(90)
t.forward(150)      # y축 그리기

t.up()
t.goto(10, 0)
t.down()

# 국어 점수 그래프 그리기
t.fillcolor('red')
t.begin_fill()
t.forward(scores[0])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[0])
t.right(90)
t.forward(20)
t.end_fill()
t.up()
t.goto(60, 0)
t.down()

# 영어 점수 그래프 그리기
t.fillcolor('green')
t.begin_fill()
t.right(90)
t.forward(scores[1])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[1])
t.right(90)
t.forward(20)
t.end_fill()

t.up()
t.goto(110, 0)
t.down()

# 수학 점수 그래프 그리기
t.fillcolor('blue')
t.begin_fill()
t.right(90)
t.forward(scores[2])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[2])
t.right(90)
t.forward(20)
t.end_fill()
