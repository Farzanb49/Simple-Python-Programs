year = str(input())
w = year[0]
x = year[1]
y = year[2]
z = year[3]
if w == x or w == y or w == z or x == y or x == z or y == z:
    print("NO")
else:
    print("YES")
    
