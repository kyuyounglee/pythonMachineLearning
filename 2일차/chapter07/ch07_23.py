import turtle
t = turtle.Turtle()
t.shape('turtle')

for i in range(1, 11):  # 원 고리를 10개 만들기
    t.circle(20)
    
    t.up()
    t.goto(i*30, 0)     # 현재 위치에서 30px씩 옆으로 이동
    t.down()
