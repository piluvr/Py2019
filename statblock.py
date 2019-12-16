import random
nlist =[]
sums=0
for i in range(6):
	for n in range(4):
		nlist.append(random.randint(1,6))
	sums=sum(nlist)
	sums +=-(min(nlist))
	print(sums)
	sums =0
	nlist.clear()
