speedlimit = int(input("Enter the speed limit: "))
speed = int(input("Enter the recorded speed of the car: "))
speedy = speed - speedlimit
if speedlimit > speed:
    print("Congratulations, you are within the speed limit!")
if speedy > 0 and speedy < 21:
    print("You are speeding and your fine is $100")
if speedy > 20 and speedy < 31:
    print("You are speeding and your fine is $270")
if speedy >= 31:
    print("You are speeding and your fine is $500")
