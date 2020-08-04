# Turtle Graphics를 이용하여 하트 모양 그리기

import turtle as t
import math as m

t.color("red")
t.begin_fill()          # line 내부를 칠하도록 명령
for x in range(100):    # 100개의 점으로 나누어 그린다
    h = m.pi*x/50
    x = 160*m.sin(h)**3
    y = 130*m.cos(h) - 50*m.cos(2*h) - 20*m.cos(3*h) - 10*m.cos(4*h)
    t.goto(x, y)        # 계산된 (x, y)위치로 거북이를 이동
t.end_fill()

t.mainloop()
