

import turtle


# players entering their name

player1_name= input("Enter your name player 1: ")       #player 1 enter their name
print("Hello", player1_name)

player2_name= input("Enter your name player 2: ")       #player2 enter their name
print("Hello", player2_name)



import Board



player1 = turtle.Turtle()
player2 = turtle.Turtle()


def characters():

    
 turtle.addshape("tiger.gif")                      #assigning player1 with the character
 player1.shape("tiger.gif")
 player1.penup()
 player1.goto(-230,-180)
 player1.towards(0,0)
 
 

 turtle.addshape("elephant.gif")                   #assigning player2 with a character
 player2.shape("elephant.gif")
 player2.penup()
 player2.goto(-230,-220)
 player2.towards(0,0)





characters()



import random

win= turtle.Turtle()
win.hideturtle()
dice = turtle.Turtle()


def main():

 player1_position = 1
 player2_position = 1
 rounds = 0
   
    
 dice.speed(0)
 dice.hideturtle
 dice.penup()
 dice.goto(0,-300)
 
 
 while True:
     input("Press enter to roll dice")
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

     if player1_position == 11:         #snake 1
        player1.goto(-230,-180)
        player1_position = 1
        
     if player1_position == 15:         #snake 2
        player1.goto(170,-80)
        player1.left(180)
        turtle.addshape("tiger1.gif")
        player1.shape("tiger1.gif")
        player1_position = 6

     if player1.position == 24:         #snake 3
        player1.goto(70,-80)
        player1.left(180)
        turtle.addshape("tiger1.gif")
        player1.shape("tiger1.gif")
        player1_position = 7

    #player 2 snake and ladder movement

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

     if player2_position == 11:         #snake 1
        player2.goto(-230,-220)
        player2_position = 1
        
     if player2_position == 15:         #snake 2
        player2.goto(170,-120)
        player2.left(180)
        turtle.addshape("elephant1.gif")
        player2.shape("elephant1.gif")
        player2_position = 6

     if player2.position == 24:         #snake 3
        player2.goto(70,-120)
        player2.left(180)
        turtle.addshape("elephant1.gif")
        player2.shape("elephant1.gif")
        player2_position = 7
      
     if(rounds % 2) == 0: 
       for a in range (Roll):
            if player1_position % 10==0:
                player1.right(90)
                player1.forward(100)
                player1.right(90)
                turtle.addshape("tiger.gif")
                player1.shape("tiger.gif")
            elif player1_position % 5 ==0:
                player1.left(90)
                player1.forward(100)
                player1.left(90)
                turtle.addshape("tiger1.gif")
                player1.shape("tiger1.gif")
            else:
             player1.forward(100*1)
            player1_position = player1_position +1

            
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

                
        
     if(rounds % 2) == 1: 
       for b in range (Roll):
            if player2_position % 10 ==0:
                player2.right(90)
                player2.forward(100)
                player2.right(90)
                turtle.addshape("elephant.gif")
                player2.shape("elephant.gif")
            elif player2_position % 5 ==0:
                player2.left(90)
                player2.forward(100)
                player2.left(90)
                turtle.addshape("elephant1.gif")
                player2.shape("elephant1.gif")
            else:
             player2.forward(100*1)
            player2_position = player2_position +1

            
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
                

     rounds = rounds + 1



    

main()


'''
        
     if player2_position == 3:
        player2.left(90)
        player2.forward(100)
        player2.left(90)
        player2_position = 8
        
     if player2_position == 12:
        player2.left(90)
        player2.forward(200)
        player2.right(90)
        player2.position = 22
        
     if player2_position == 16:
        player2.left(90)
        player2.forward(100)
        player2.right(90)
        player2.position = 25

     if player2_position == 11:
        player2.right(90)
        player2.forward(200)
        player2.towards(90,0)
        player2.position = 1
        
     if player2_position == 15:
        player2.left(90)
        player2.forward(100)
        player2.right(90)
        player2.position = 6

     if player2.position == 24:
        player2.right(90)
        player2.forward(300)
        player2.right(90)
        player2.position = 7
        
        '''


'''
def main():
    
    if(rounds % 2) == 0:
        for a in range (0, Roll):
            if player1_position % 10==0:
                player1.right(90)
                player1.forward(100)
                player1.right(90)
            elif player1_position % 5 ==0:
                player1.left(90)
                player1.forward(100)
                player.left(90)
            else:
                player1.forward(100*1)
            player1_position = player1_position +1
            if player1_postion == 25:
                win.showturtle()
                turtle.addshape("win.gif")
                win.shape("win.gif")
                print(player1, "wins")



'''





'''
 dice.speed(0)
 dice.hideturtle
 dice.penup()
 dice.goto(0,-300)

 
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
  




def main():

 
    
    rolldice = input("Press enter to roll dice")

    print (roll())
    

    


main()







'''
'''
import random

roll = random.randint(1,6)
dice = turtle.Turtle()



def dice_roll():
    

 turtle.addshape("dice1.gif")
 turtle.addshape("dice2.gif")
 turtle.addshape("dice3.gif")
 turtle.addshape("dice4.gif")
 turtle.addshape("dice5.gif")
 turtle.addshape("dice6.gif")

 dice.speed(0)
 dice.hideturtle
 dice.penup() 
 dice.goto(0,-300)



def dice_display():
 dice.st()
if (roll==1):
     dice.shape("dice1.gif")
elif(roll==2): 
     dice.shape("dice2.gif")
elif(roll==3):  
     dice.shape("dice3.gif")
elif(roll==4):
     dice.shape("dice4.gif")
elif(roll==5):
     dice.shape("dice5.gif")
elif(roll==6):
     dice.shape("dice6.gif")
  

dice_display()


def main():

    rolldice = input("Press enter to roll dice")
    print (roll())


import random


def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll




main()


'''








'''
def characters():

#assigning players to characters

 player1=turtle.Turtle()

 turtle.addshape("tiger.gif")                      #assigning player1 with the character
 player1.shape("tiger.gif")
 player1.penup()
 player1.goto(-240,-180)

     
 player2=turtle.Turtle()

 turtle.addshape("elephant.gif")                   #assigning player2 with a character
 player2.shape("elephant.gif")
 player2.penup()
 player2.goto(-240,-220)


characters()




def startgame():
    rolldice = input("Press enter to roll dice")
    
 
  
import random

Roll = random.randint(1,2)

def roll():
    print(Roll())

turtle.addshape("dice1.gif")
turtle.addshape("dice2.gif")
turtle.addshape("dice3.gif")
turtle.addshape("dice4.gif")
turtle.addshape("dice5.gif")
turtle.addshape("dice6.gif")

dice=turtle.Turtle()
dice.speed(0)
dice.hideturtle
dice.penup()
dice.goto(0,-300)


startgame()


def dice_display():
 dice.st()
if (Roll==1):
     dice.shape("dice1.gif")
elif(Roll==2): 
     dice.shape("dice2.gif")
elif(Roll==3):  
     dice.shape("dice3.gif")
elif(Roll==4):
     dice.shape("dice4.gif")
elif(Roll==5):
     dice5.shape("dice5.gif")
elif(Roll==6):
     dice6.shape("dice6.gif")
  

dice_display()



'''




