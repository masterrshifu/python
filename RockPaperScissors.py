from random import randint
moves = ["Rock", "Paper", "Scissor"]
computer = moves[randint(0,2)]
player = False
while player == False:
    userMove = input("Rock, Paper, Scissors? Please enter your move! \n Enter Quit to exit!")
    if userMove == computer:
        print("Tie!")
    elif userMove == "Rock":
        if computer == "Paper":
            print("You lose!",computer,"covers",userMove)
        else:
            print("You win",userMove,"smashes",computer)
    elif userMove == "Paper":
        if computer == "Scissors":
            print("You lose!",computer,"cuts",userMove)
        else:
            print("You win",userMove,"covers",computer)
    elif userMove == "Scissors":
        if computer == "Rock":
            print("You lose!",computer,"smashes",userMove)
        else:
            print("You lose!",userMove,"cuts",computer)
    elif userMove == "Quit":
        print("Thanks for playing Rock, Paper and Scissors!")
        player = True
        break
    else:
        print("This is not a valid play! Check your spelling!")
    computer = moves[randint(0,2)]
    

