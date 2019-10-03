#bincon.py  Kenny
#decimal to binary algorithm
i=int(input("enter a decimal value less than 256: "))
k=0
h=128
l=""
while h>1:
	if i > 256 or i < 0:
		print("input a valid number!")
		break
	
	k=i%h
	if i/h >=0:
		k=str(i/h)
		i=int(i/h)
		h=int(h/2)
		l=l+k
		print(h)
	
print(l)
