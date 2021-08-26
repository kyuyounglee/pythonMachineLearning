import turtle
t = turtle.Turtle()
t.shape("turtle")


t.fillcolor('red')  # 색상('red')을 설정한다.
t.begin_fill()      # 채색 시작
t.circle(50)   
t.end_fill()        # 채색 끝

t.up()          
t.goto(120, 0)  
t.down()        


t.circle(50)    
t.end_fill()          # 채색 끝
