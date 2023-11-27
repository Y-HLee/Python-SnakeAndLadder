

import turtle


# players entering their name

player1_name= input("Enter your name player 1: ")       #player 1 enter their name
print("Hello", player1_name, "you are tiger.")

player2_name= input("Enter your name player 2: ")       #player2 enter their name
print("Hello", player2_name, "you are elephant.")



import Board



player1 = turtle.Turtle()
player2 = turtle.Turtle()


def characters():

    
 turtle.addshape("tiger.gif")                      #assigning player1 with the character and giving the starting position 
 player1.shape("tiger.gif")
 player1.penup()
 player1.goto(-230,-180)
 player1.setheading(0)
 
 

 turtle.addshape("elephant.gif")                   #assigning player2 with a character and giving the starting position 
 player2.shape("elephant.gif")
 player2.penup()
 player2.goto(-230,-220)
 player2.setheading(0)





characters()



import random

win= turtle.Turtle()                        #assigning win.gif to a turtle
win.hideturtle()
dice = turtle.Turtle()                      #assigning dice to a turtle


def main():                                 #main function
 
 player1_position = 1                       #player 1 and 2 positioning and rounds
 player2_position = 1
 rounds = 0
   
    
 dice.speed(0)                              #dice positioning
 dice.hideturtle
 dice.penup()
 dice.goto(0,-300)
 
 
 while True:
     input("Press enter to roll dice")      #assigning different dice pictures to the roll
     Roll = random.randint(1,6)
     print(Roll)
     if (Roll==1): 
      turtle.addshape("dice1.gif")
      dice.shape("dice1.gif")
     elif(Roll==2):
      turtle.addshape("dice2.gif")
      dice.shape("dice2.gif")
     elif(Roll==3):
      turtle.addshape("dice3.gif")
      dice.shape("dice3.gif")
     elif(Roll==4):
      turtle.addshape("dice4.gif")
      dice.shape("dice4.gif")
     elif(Roll==5):
      turtle.addshape("dice5.gif")
      dice.shape("dice5.gif")
     elif(Roll==6):
      turtle.addshape("dice6.gif")
      dice.shape("dice6.gif")

     
      
     if(rounds % 2) == 0:                              #player 1 movement
       for a in range (Roll):
            if player1_position % 10==0:               #if player1 lands on box in division of 10, the player goes up 
                player1.right(90)
                player1.forward(100)
                player1.right(90)
                turtle.addshape("tiger.gif")
                player1.shape("tiger.gif")
            elif player1_position % 5 ==0:             #if player1 lands on box in division of 5, the player goes up 
                player1.left(90)
                player1.forward(100)
                player1.left(90)
                turtle.addshape("tiger1.gif")
                player1.shape("tiger1.gif")
            else:
             player1.forward(100*1)
            player1_position = player1_position +1

            
            if player1_position == 25:                  #when player1 lands on box 25 they are the winner
                win.showturtle()
                turtle.addshape("win.gif")
                win.shape("win.gif")
                print(player1_name, "wins")

                replay = input("Would you like to play again? yes/ no")
                if replay == "yes":
                    win.undo()
                    characters()
                    main()
                    player1_position = 1
                    player2_position = 1
                    continue
                else:
                    exit()

                
        
     if(rounds % 2) == 1:                               #player 2 movement
       for b in range (Roll):
            if player2_position % 10 ==0:               #if player2 lands on box in division of 10, the player goes up 
                player2.right(90)
                player2.forward(100)
                player2.right(90)
                turtle.addshape("elephant.gif")
                player2.shape("elephant.gif")
            elif player2_position % 5 ==0:              #if player2 lands on box in division of 5, the player goes up 
                player2.left(90)
                player2.forward(100)
                player2.left(90)
                turtle.addshape("elephant1.gif")
                player2.shape("elephant1.gif")
            else:
             player2.forward(100*1)
            player2_position = player2_position +1

            
            if player2_position == 25:                  #when player2 lands on box 25 they are the winner
                win.showturtle()
                turtle.addshape("win.gif")
                win.shape("win.gif")
                print(player2_name, "wins")

                replay = input("Would you like to play again? yes/ no")
                if replay == "yes":
                    win.undo()
                    characters()
                    main()
                    player1_position = 1
                    player2_position = 1
                    continue
                else:
                    exit()

     #player1 ladder movement
                    
     if player1_position == 3:          #ladder 1
        player1.goto(-30,-80)
        player1.left(180)
        turtle.addshape("tiger1.gif")
        player1.shape("tiger1.gif")
        player1_position = 8
        
     if player1_position == 12:         #ladder 2
        player1.goto(-130,220)
        turtle.addshape("tiger.gif")
        player1.shape("tiger.gif")
        player1_position = 22
        
     if player1_position == 16:         #ladder 3
        player1.goto(170,220)
        player1.right(180)
        turtle.addshape("tiger.gif")
        player1.shape("tiger.gif")
        player1_position = 25
        
        if player1_position == 25:
            win.showturtle()
            turtle.addshape("win.gif")
            win.shape("win.gif")
            print(player1_name, "wins")

            replay = input("Would you like to play again? yes/ no")
            if replay == "yes":
                win.undo()
                characters()
                main()
                player1_position = 1
                player2_position = 1
                continue
            else:
                exit()

     #player1 snake movement

     if player1_position == 11:         #snake 1
        player1.goto(-230,-180)
        player1_position = 1
        
     if player1_position == 15:         #snake 2
        player1.goto(170,-80)
        player1.left(180)
        turtle.addshape("tiger1.gif")
        player1.shape("tiger1.gif")
        player1_position = 6

     if player1_position == 24:         #snake 3
        player1.goto(70,-80)
        player1.left(180)
        turtle.addshape("tiger1.gif")
        player1.shape("tiger1.gif")
        player1_position = 7

    #player 2 ladder movement

     if player2_position == 3:          #ladder 1
        player2.goto(-30,-120)
        player2.left(180)
        turtle.addshape("elephant1.gif")
        player2.shape("elephant1.gif")
        player2_position = 8
        
     if player2_position == 12:         #ladder 2
        player2.goto(-130,180)
        turtle.addshape("elephant.gif")
        player2.shape("elephant.gif")
        player2_position = 22
        
     if player2_position == 16:         #ladder 3
        player2.goto(170,180)
        player2.right(180)
        turtle.addshape("elephant.gif")
        player2.shape("elephant.gif")
        player2_position = 25
        
        if player2_position == 25:
            win.showturtle()
            turtle.addshape("win.gif")
            win.shape("win.gif")
            print(player2_name, "wins")

            replay = input("Would you like to play again? yes/ no")
            if replay == "yes":
                win.undo()
                characters()
                main()
                player1_position = 1
                player2_position = 1
                continue
            else:
                exit()

     #player 2 snake movement

     if player2_position == 11:         #snake 1
        player2.goto(-230,-220)
        player2_position = 1
        
     if player2_position == 15:         #snake 2
        player2.goto(170,-120)
        player2.left(180)
        turtle.addshape("elephant1.gif")
        player2.shape("elephant1.gif")
        player2_position = 6

     if player2_position == 24:         #snake 3
        player2.goto(70,-120)
        player2.left(180)
        turtle.addshape("elephant1.gif")
        player2.shape("elephant1.gif")
        player2_position = 7


        
     rounds = rounds + 1




main()


