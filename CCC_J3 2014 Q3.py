n=int(input())

antonia = 100
david = 100

for x in range(n):
    roll = input().split()
    a = int(roll[0])
    d = int(roll[1])
    if a < d:
        antonia = antonia - d
    elif d < a:
        david = david -a

print (antonia)
print (david)

    
    
    

