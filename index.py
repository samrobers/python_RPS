import random 

compChoice = ""

def get_ComputerMove():
    compChoice = random.randint(1,3)
    if compChoice == 1 :
        compChoice = "rock"
        print(compChoice)
    elif compChoice == 2: 
        compChoice = "paper"
        print(compChoice)
    elif compChoice == 3:
        compChoice = "scissors"
        print(compChoice)
    else: 
        print("The wrong numbers are being generated")

def get_PlayerMove():
     playerChoice = input("RPS area, please type rock, paper, or scissors: ")

        
def calculateWinner():
    



def Main(): 