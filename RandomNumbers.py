import random
from datetime import date
import subprocess
today = date.today()
thisDate = today.strftime("%Y-%m-%d")
f= open(thisDate+".txt","w")
s=""
for i in range (0,65536):
	n = random.randint(65, 90)
	c = chr(n)
	if(i%100 ==0):
		s+="\n" + c
	else:
		s += c
f.write(s)	
f.close()	
subprocess.call("./sendfile.sh", shell=True)
