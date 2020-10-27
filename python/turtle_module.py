import turtle
import time
import re

question  = input('What you want to Do? ')
skk = turtle.Pen()

if question.find('draw') != -1:
            

       skk.pensize(4)

       skk.penup()
       skk.goto(-200,120)

       # Drawing G
       skk.pendown()
       skk.backward(50)

       skk.right(90) 
       skk.forward(70)

       skk.left(90)
       skk.forward(30)

       skk.left(90)
       skk.forward(30)

       skk.right(90)
       skk.forward(20)

       skk.right(90)
       skk.forward(30)

       #Moving pen

       skk.penup()
       skk.goto(-160,120)

       #Drwaing O
       skk.pendown()
       skk.forward(70)

       skk.left(90)
       skk.forward(40)

       skk.left(90)
       skk.forward(70)

       skk.left(90)
       skk.forward(40)


       #Drawing u
       skk.penup()
       skk.goto(-80,120)


       skk.pendown()


       skk.left(90)
       skk.forward(70)

       skk.left(90)
       skk.forward(40)

       skk.left(90)
       skk.forward(70)

       #Drawing R

       skk.penup()
       skk.goto(0,50)

       skk.pendown()
       skk.forward(70)

       skk.right(90)
       skk.forward(40)

       skk.right(90)
       skk.forward(40)

       skk.right(90)
       skk.forward(40)


       skk.goto(40,50)
       skk.penup()

       #Drawing A

       skk.goto(80,50)

       skk.pendown()
       skk.right(90)
       skk.forward(70)

       skk.right(90)
       skk.forward(40)

       skk.right(90)
       skk.forward(70)


       skk.penup()
       skk.goto(80,80)


       skk.pendown()
       skk.left(90)
       skk.forward(40)

       #Drawing v
       skk.penup()

       skk.goto(160,120)
       skk.pendown()

       skk.right(60)
       skk.goto(180,50)

       skk.goto(200,120)
 
       time.sleep(1)
       turtle.Screen().bye()

else:
       print('Sorry try something else')
       
question = input('What else you want ot do')
     



print('whsdfds')
