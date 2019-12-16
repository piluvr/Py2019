# dechex1.py Kenny
def hexcon(num):
	HexString =""
	Key = "0123456789ABCDEF"	
	if(num //16 >= 1):
		HexString+=str(Key[num // 16])
		HexString+=str(Key[num % 16])
		num = num % 16
		return HexString
	else:
		HexString+=str(Key[num % 16])
		num = num % 16
		return HexString	
def bincon(n): 
    return bin(n).replace("0b","") 
def main():	
	ASCIIKEY=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz|~'
	io=int(input("input a number lower than 255: "))
	Newkey=""
	if(io>=32  and io <127):
		Newkey=str(ASCIIKEY[io-32])
	#print(type(io))
	#print(type(bincon(io)))
	#print(type(hexcon(io)))
	#print(type(Newkey))
	print(str(io)+" "+bincon(io)+" "+hexcon(io)+" "+Newkey)
		
main()
