# your code goes here
feet = int(input("Enter the Feet for the first piece of fabric:"))
inches = int(input("Enter the Inches for the first piece of fabric:"))

feet2 = int(input("Enter the Feet for the second piece of fabric:"))
inches2 = int(input("Enter the Inches for the second piece of fabric:"))

final1= ((feet + feet2)+(((inches1+inches2)%12))
final2= ((inches1 + inches2)-(((inches1+inches2)%12))*12)
print("Feet: " + final1 + " Inches: " + final2)
