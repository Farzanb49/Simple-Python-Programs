x = int(input("Enter the first angle: "))
y = int(input("Enter the second angle: "))
z = int(input("Enter the third angle: "))
if x+y+z==180:
    if x==y==z==60:
        print("Equilateral")
    elif x==y or y==z or x==z:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
        
