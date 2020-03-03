from termcolor import colored #api for colored font
for n in range(1,101): #increments counting variable
	if(n%3==0 and n%5!=0): #checks if compatible with one condition and not the other
		print(colored("fizz","blue"))
	elif(n%5==0 and n%3!=0): #same here
		print(colored("buzz","green"))
	elif(n%5==0 and n%3==0): #checks if both are compatible
		print(colored("fizz", "blue") + colored("buzz","green"))
	else: #if none are compatible
		print(colored(str(n),"red"))
