v = int(input())
votes = input()

# in python the following loop could be replaced with
# acount = votes.count("A")
acount = 0
for letter in votes:
    if letter == "A":
        acount = acount + 1

bcount = v - acount
if acount > bcount:
    print ("A")
elif bcount > acount:
    print ("B")
else:
    print ("Tie")
        
        
    
