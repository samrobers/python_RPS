import random 

playerChoice = ""
compChoice = ""
playGame = ""
def get_ComputerMove():
            global compChoice
            compChoice = random.randint(1,3)
            if compChoice == 1:
                compChoice = "rock"
            elif compChoice == 2: 
                compChoice = "paper"
                print(compChoice)
            elif compChoice == 3:
                compChoice = "scissors"
                print(compChoice)
def get_PlayerMove():
             global playerChoice
             playerChoice = input("RPS area, please type rock, paper, or scissors: ")
             
def calculateWinner():
            if compChoice == playerChoice :     
                print("The computer chose " + compChoice + " It is a tie.")
                Main()
            elif compChoice == "rock" and playerChoice != "paper":    
                print("The computer chose " + compChoice + " You lose.")
                Main()
            elif compChoice == "paper" and playerChoice != "scissors":    
                print("The computer chose " + compChoice + " You lose.")
                Main()
            elif compChoice == "scissors" and playerChoice != "rock":    
                print("The computer chose " + compChoice + " You lose.")
                Main()
            else: 
                print("The computer chose " + compChoice + " You Win.")
                Main()
def Main():
    global playGame
    playGame = input("Would you like to play RPS, yes or no: ")
    while playGame == "yes":
            if compChoice != "rock" or "paper" or "scissors":
                get_ComputerMove()
            if playerChoice != "rock" or "paper" or "scissors":
                get_PlayerMove()
            if compChoice == "rock" or "paper" or "scissors" and playerChoice =="rock" or "paper" or "scissors":
                calculateWinner() 
                            
Main()
        


