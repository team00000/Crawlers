import turtle
from turtle import *
import time


def heart():#此简单函数的目的就是不断的移动画笔
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
#love=input('XXX')
#me=input('XXX')
turtle.setup(width=900,height=500)#确定画布
turtle.speed(2)#确定笔速
turtle.pensize(3)#确定画出的线条尺寸
turtle.color('red','red')#第一个颜色为画笔画出来的颜色，第二个为背景填充色
turtle.up()
turtle.hideturtle()
turtle.goto(0,-100)#移动
turtle.showturtle()
turtle.down()#下笔画图
turtle.speed(2)
turtle.begin_fill()
turtle.left(140)#指定移动角度
turtle.forward(110.25)#指定在移动角度的范围内，移动的线条距离
heart()#开始画笔往右移动，此时应该到达心  图案的凹槽处
turtle.left(120)#再从凹槽处进行一个弧度  其实就是右半边的心
heart()#画笔开始右移
turtle.forward(110.25)#移动距离和上述的相同，这样才能封心  下方的尖
turtle.end_fill()

turtle.pensize(5)
turtle.up()
turtle.hideturtle()
turtle.goto(0,0)
turtle.showturtle()
turtle.color('black','pink')
turtle.write('best wishes to CLE',font=('gungsuh',12),align="center")#写入内容
turtle.up()
turtle.hideturtle()
time.sleep(0.5)

turtle.pensize(5)
turtle.up()
turtle.hideturtle()
turtle.goto(0,0)
turtle.showturtle()
turtle.color('white','pink')
turtle.write('best wishes to CLE',font=('gungsuh',12),align="center")
turtle.up()
turtle.hideturtle()
time.sleep(0.5)

turtle.pensize(5)
turtle.up()
turtle.hideturtle()
turtle.goto(0,0)
turtle.showturtle()
turtle.color('yellow','pink')
turtle.write('best wishes to CLE',font=('gungsuh',12),align="center")
turtle.up()
turtle.hideturtle()
time.sleep(3)#上述程序写了三遍，利用了不同颜色，这样可以呈现一闪一闪的效果


turtle.color('black','pink')
turtle.goto(100,-100)
turtle.showturtle()
turtle.speed(5)
turtle.write('from your fans', font=(20,), align="center", move=True)#落款


#点击关闭窗口

window=turtle.Screen()
window.exitonclick()#点击跳出的窗口，窗口即可关闭