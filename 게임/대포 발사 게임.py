# 대포 발사 게임
# 게임방법: 키보드 위/아래 방향키로 각도를 조절하고 spacebar를 눌러 발사

import turtle as t
import random

def turn_up():
  t.left(2)

def turn_down():
  t.right(2)

def fire():             # 스페이스바 누르면 거북이 대포 발사
  ang = t.heading()     # 현재 거북이가 바라보는 각도 기억
  while t.ycor()>0:     # 거북이가 땅 위에 있는 동안 반복
    t.forward(15)
    t.right(5)
    # while 반복문을 빠져나오면 거북이가 땅에 닿은 것임
    
  d = t.distance(target, 0)         # 거북이와 목표 지점과의 거리를 구함
  t.sety(random.randint(10, 100))   # 성공 또는 실패 메시지를 표시할 위치를 정함
  if d<25:                          # 거리 차이가 25보다 작으면 성공으로 간주
    t.color("blue")
    t.write("Good!", False, "center", ("", 15))
  else:
    t.color("red")
    t.write("Bad!", False, "center", ("", 15))
  t.color("black")
  t.goto(-200, 10)    # 거북이 위치를 처음 발사했던 곳으로 되돌림
  t.setheading(ang)   # 각도도 처음 기억해둔 각도로 되돌림

# 땅을 그립니다
t.goto(-300, 0)
t.down()
t.goto(300, 0)

# 목표 지점을 설정하고 그립니다
target = random.randint(50, 150)    # 목표 지점 50~150사이에서 임의로 지정
t.pensize(3)
t.color("green")
t.up()
t.goto(target-25, 2)
t.down()
t.goto(target+25, 2)
  
# 거북이 색상을 검은색으로 지정하고 처음 발사했던 곳으로 되돌립니다
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# 거북이가 동작하는데 필요한 설정을 합니다
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()          # 거북이 그래픽 창이 키보드 입력을 받습니다
