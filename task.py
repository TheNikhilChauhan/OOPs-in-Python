from turtle import *

p = Turtle()

colors = ["red", "blue", "purple", "green", "yellow", "lime green"]

for i in range(6):
    p.color(colors[i])
    p.width(5)
    p.fd(100)
    p.rt(60)

done()