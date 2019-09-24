# your code goes here
hour = int(input("Enter the hour: "))
min = int(input("Enter the minute: "))
min +=15
if min - 60 >= 0:
	min += -60
	hour +=1
if hour -12 > 0:
	hour +=-12
print("Hours: " + str(hour))
print("Minutes: " + str(min))
