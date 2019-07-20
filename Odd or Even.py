a = int(input("enter number here: "))
if a % 2 == 0 and not a % 4 == 0:
	print ("This is an even number")
elif a % 4 == 0:
	print ("This number is the GOAT")
else:
	print ("This is an odd number")
num = int(input("enter a new number here: "))
check = int(input("enter another new number here: "))
if num % check == 0:
    print ("num is divisible by check")
else:
    print ("num is not divisible by check")
