from turtle import *
# speed(500)
# bgcolor('black')
# r,g,b=255,0,0
# for i in  range(255*2):
#     colormode(255)
#     if i<255//3:
#         g+= 3
#     elif i<255*2//3:
#         r-=3
#     elif i<255:
#         b+=3
#     elif i<255*4//3:
#         g-=3
#     elif i<255*5//3:
#         r+=3
#     else:
#         b-=3
#     fd(50+i)
#     rt(91)
#     pencolor(r,g,b)
# import turtle

# colors = [ "red","purple","blue","green","orange","yellow"]
# my_pen = turtle.Pen()
# turtle.bgcolor("black")
# for x in range(360):
#    my_pen.pencolor(colors[x % 6])
#    my_pen.width(x/100 + 1)
#    my_pen.forward(x)
#    my_pen.left(59)



import turtle
speed(500)
my_wn = turtle.Screen()
turtle.speed(2)
for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()