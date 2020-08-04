import turtle as t

n=5

t.color("purple")
t.pensize(3)

t.begin_fill()

# 오각형
for x in range(n):
    t.forward(50)
    t.left(360/n)

t.end_fill()


t.penup()           # 펜을 떼고
t.forward(250)      # 자리 이동
t.down()            # 펜 붙이고


t.begin_fill()

# 사각형
for x in range(n-1):
    t.forward(50)
    t.left(360/(n-1))

t.end_fill()
