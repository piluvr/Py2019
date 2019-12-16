import random
from colorama import init 
from termcolor import colored 
'''
	If you are running this code on a fresh install, do this:
	1. sudo apt install python3-pip
	2. pip3 install termcolor
    Roll any other number but one you add it to your turn total and keep rolling until you roll a 1.
    If you roll a 1, no score and it becomes the next player's turn. Basically you lose your turn total points.
    The player can choose to hold. This means their turn total is added to their score and it becomes the next player's turn.
    The first person to score 100 or above wins.
'''
init()
n=0
score=0
tempscore=0
choice= "heeeheee"
player = 3
cpuchoice=1
while(score <100):
	if( player==1):
		choice= input(colored("Player " +str(player)+", R to roll, H to hold "))
		choice= choice.lower()
		if(choice == "r"):
			n=random.randint(1,6) 
			if(n==1):
				tempscore =0
				print(colored("you got a 1, so your score for this turn is reset!", "blue"))
				if(player == 1):
					player =2
				else:
					player =1
			else:
				print(colored("you got a "+ str(n), "blue"))
				tempscore+=n
		elif(choice == "h"):
			score+=tempscore
			tempscore=0
			print(colored("the score is " +str(score), "green"))
			if(score<100):
				if(player == 1):
					player =2
				else:
					player =1
	else:
		cpuchoice=(random.randint(0,100))
		if(tempscore!=0):
			choice="r"
		elif(cpuchoice>=score-100):
			choice="h"
		else:
			choice="r"
		
		if(choice == "r"):
			n=random.randint(1,6) 
			if(n==1):
				tempscore = 500
				print(colored("the cpu got a 1, so their score for this turn is reset!", "red"))
				if(player == 1):
					player =2
				else:
					player =1
			else:
				print(colored("the cpu got a "+ str(n), "red"))
				tempscore+=-n
		elif(choice == "h"):
			score+=tempscore
			print(colored("the score is " +str(score), "green"))
			if(score<100):
				if(player == 1):
					player =2
				else:
					player =1	
						
print(colored("Player " +str(player)+" Wins!","yellow"))		
