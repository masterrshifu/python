import random
print(" Welcome to Rock/Paper/Scissor game ")
userscore=0
computerscore=0
flag = True
while(flag == True):
    userMove = input("Rock, Paper, Scissors? Please enter your move! \nEnter Quit to exit!: ")
    options = ["Rock","Paper", "Scissors"]
    computerMove = random.choice(options)
    if(userMove == computerMove):
        print("Tie")
        userscore += 1
        computerscore += 1
    elif(userMove == "Scissors"):
        if(computerMove == "Paper"):
            print("User won against Computer")
            userscore += 2
        else:
            print("Computer won against User")
            computerscore += 2
    elif(userMove == "Rock"):
        if(computerMove == "Scissors"):
            print("User won against Computer")
            userscore += 2
        else:
            print("Computer won against User")
            computerscore += 2
    elif(userMove == "Paper"):
        if(computerMove == "Rock"):
            print("User won against Computer")
            userscore += 2
        else:
            print("Computer won against User")
            computerscore += 2
            print("UserScore is ", userscore)
            print("ComputerScore is ", computerscore)
    elif(userMove == "Quit"):
        flag = False
        print("Thanks for playing the game")
        if(userscore == computerscore):
            print("User and Computer tied the game scoring same points : ", userscore)    
            break
        elif(userscore > computerscore):
            difference = userscore - computerscore
            print("User won against the computer by", difference, "points" )
            break
        else:
            difference = computerscore - userscore
            print("Computer won against the User by" , difference, "points" )
            break
    else:
            print("Invalid Option, Choose the right input")
    print("Computer Score: ",computerscore)
    print("User Score: ",userscore)
        
        
