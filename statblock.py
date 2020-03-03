import random
nlist =[]
sums=0

for i in range(6):
	for n in range(4):
		if(random.randint(1,6) ==1):
			num = random.randint(1,6)
			nlist.append(num)
		else:
			nlist.append(random.randint(1,6))
	sums=sum(nlist)
	sums +=-(min(nlist))
	print(sums)
	sums =0
	nlist.clear()
