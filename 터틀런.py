# 터틀런 게임
# 게임방법: 키보드를 이용하여 빨간색 악당 거북이를 피해 녹색 먹이를 먹는 게임

import turtle as t
import random

score = 0               # 점수를 저장하는 변수
playing = False         # 현재 게임이 플레이 중인지 확인하는 변수

te = t.Turtle()         # 악당 거북이(빨간색)
te.color("red")
te.shape("turtle")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()         # 먹이(초록원)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

def start():                # 게임을 시작하는 함수
    global playing
    if playing == False:
        playing = True
        t.clear()           # 메시지를 지움
        play()

def play():                 # 게임을 실제로 플레이 하는 함수
    global score
    global playing
    t.forward(10)                       # 주인공거북이 10 앞으로
    if random.randint(1, 5) == 3:       # 1~5 사이에서 뽑은 수가 3이면(20% 확률)
        ang = te.towards(t.pos())
        te.setheading(ang)              # 악당 거북이가 주인공 거북이를 바라봄
    speed = score + 5                   # 점수 획득마다 악당 거북이 속도 증가

    if speed >  15:                     # 악당거북이 최대속도 15
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12:             # 주인공과 악당의 거리가 12보다 작으면 게임 종료
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(ts) < 12:             # 주인공과 먹이의 거리가 12보다 작으면(가까우면)
        score = score + 1               # 점수를 올림
        t.write(score)                  # 점수를 화면에 표시
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮김
    if playing:
        t.ontimer(play, 100)            # 게임 플레이 중이면 100ms마다 play 함수 반복실행

def message(m1, m2):        # 메시지를 화면에 표시하는 함수
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()                          # 거북이 그래픽 창이 키보드 입력을 받도록 함
message("Turtle Run", "[Space]")
