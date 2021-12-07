import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("-> Enter choice among \n   Rock, Paper or  Scissors: ").capitalize()
    if player == computer:
        print("\n   Computer selected ",computer,"\n")
        print("   Tie!\n")
        print("   If you want to end the game,then enter END if not then enter the choice again\n")
    ## Conditions of Rock,Paper and Scissors if player == computer:
        print("\n   Computer selected ",computer,"\n")
        print("   Tie!\n")
        print("   If you want to end the game,then enter END if not then enter the choice again\n")
    elif player == "Rock":
        if computer == "Paper":
            print("\n   Computer selected paper\n")
            print("   You lose! =>", computer, "covers", player,"\n")
            cpu_score+=1
            print("   If you want to end the game,then enter END if not then enter the choice again\n")  
        else:
            print("\n   Computer selected Scissors\n")
            print("   You win! =>", player, "smashes", computer,"\n")
            player_score+=1
            print("   If you want to end the game,then enter END if not then enter the choice again\n")
            
    elif player == "Paper":
        if computer == "Scissors":
            print("\n   Computer selected Scissors\n")
            print("   You lose! =>", computer, "cut", player,"\n")
            cpu_score+=1
            print("   If you want to end the game,then enter END if not then enter the choice again\n") 
        else:
            print("\n   Computer selected Rock\n")
            print("   You win! =>", player, "covers", computer,"\n")
            player_score+=1
            print("   If you want to end the game,then enter END if not then enter the choice again\n")
            
    elif player == "Scissors":
        if computer == "Rock":
            print("\n   Computer selected Rock\n")
            print("   You lose! =>", computer, "smashes", player,"\n")
            cpu_score+=1
            print("   If you want to end the game,then enter END if not then enter the choice again\n")  
        else:
            print("\n   Computer selected Paper\n")
            print("   You win! =>", player, "cut", computer,"\n")
            player_score+=1
            print("   If you want to end the game,then enter END if not then enter the choice again\n")
    
    elif player=='End':
        print("\nFinal Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break