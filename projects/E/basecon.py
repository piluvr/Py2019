#basecon.py Kenny
def bincon(num,addSpace):
	n = num
	s = addSpace
	#print(n,s) #debug 
	d = 128
	binString ="" #create a string called binString
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		#print(d,q,r) debug line
		n = r
		d = int(d / 2)
		binString = binString+str(q)
		if(s == 1 and i==3):
			binString += " "
	print(binString)	
	
def main():
	bincon(191,0)
	bincon(7,1)
	inputnum= int(input("enter a number: "))
	inputspace = int(input("1 for space, 0 for no space: "))
	bincon(inputnum,inputspace)

main()
