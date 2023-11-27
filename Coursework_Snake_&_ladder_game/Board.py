import turtle



def the_board():

 #board drawing 

 turtle.bgcolor("#a1fd85")
 turtle.setup(800,800)
 t1=turtle.Turtle()
 t2=turtle.Turtle()
 t1.hideturtle()
 t2.hideturtle()
 t1.penup()
 t2.penup()
 t1.pensize(3)
 t2.pensize(3)
 t1.speed(0)
 t2.speed(0)
 t1.left(90)
 for i in range(6):
     t1.goto(-250+(100*i),-250)  #t1 turtle is drawing the vertical lines
     t1.pendown()
     t1.forward(500)
     t1.penup()
     t2.goto(250,250-(100*i))    #t2 turtle is drawing the horizontal lines 
     t2.pendown()
     t2.backward(500)
     t2.penup()


def numbers():

 #placing the numbers on the board   

 t3=turtle.Turtle()
 t3.hideturtle()
 t3.color("red")
 t3.speed(0)
 t3.penup()
 t3.goto(-240,-180)
 for i in range(25):
     t3.write(i+1,font=5)
     t3.forward(100)
     if (i+1)%10==0:
         t3.right(90)
         t3.forward(100)
         t3.right(90)
         t3.forward(100)
     elif (i+1)%5==0:
         t3.left(90)
         t3.forward(100)
         t3.left(90)
         t3.forward(100)


         
def pictures():

 #placing the numbers on the board 
 
 t4=turtle.Turtle()
 t5=turtle.Turtle()
 t6=turtle.Turtle()
 t7=turtle.Turtle()
 t8=turtle.Turtle()
 t9=turtle.Turtle()

 t4.hideturtle()
 t4.penup()
 t4.goto(-100,60)
 t4.showturtle()
 turtle.addshape("vine1.gif")
 t4.shape("vine1.gif")

 t5.hideturtle()
 t5.penup()
 t5.goto(200,80)
 t5.showturtle()
 turtle.addshape("vine2.gif")
 t5.shape("vine2.gif")

 t6.hideturtle()
 t6.penup()
 t6.goto(0,-220)
 t6.showturtle()
 turtle.addshape("vine3.gif")
 t6.shape("vine3.gif")

 t7.hideturtle()
 t7.penup()
 t7.goto(-190,-120)
 t7.showturtle()
 turtle.addshape("snake.gif")
 t7.shape("snake.gif")

 t8.hideturtle()
 t8.penup()
 t8.goto(200,-60)
 t8.showturtle()
 turtle.addshape("snake2.gif")
 t8.shape("snake2.gif")

 t9.hideturtle()
 t9.penup()
 t9.goto(100,60)
 t9.showturtle()
 turtle.addshape("snake3.gif")
 t9.shape("snake3.gif")



 
the_board()
numbers()
pictures()
