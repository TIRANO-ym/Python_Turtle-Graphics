import turtle as t

t.bgcolor("black")    # 배경색
t.speed(0)

for x in range(200):
  if x%3 == 0:
    t.color("red")
  if x%3 == 1:
    t.color("yellow")
  if x%3 == 2:
    t.color("blue")
    
  t.forward(x*2)      # 반복하면서 선이 점차적으로 길어짐
  t.left(119)         # 119도 왼쪽으로 회전
