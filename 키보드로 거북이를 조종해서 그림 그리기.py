import turtle as t

def turn_right():   # 오른쪽으로 이동하는 함수
  t.setheading(0)   # t.seth(0)으로 입력해도 됨
  t.forward(10)     # t.fd(10)으로 입력해도 됨

def turn_up():
  t.setheading(90)
  t.forward(10)

def turn_left():
  t.setheading(180)
  t.forward(10)

def turn_down():
  t.setheading(270)
  t.forward(10)

def blank():
  t.clear()

t.shape("turtle")                 # 커서의 모양을 거북이 모양으로 변경
t.speed(0)
t.onkeypress(turn_right, "Right") # 오른쪽 방향키를 누르면 turn_right 함수 실행
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")     # ESC를 누르면 blank 함수 실행
t.listen()                        # 그래픽 창에서 키보드 입력을 기다림
