import datetime

now = datetime.datetime.now()

print
print ("Current date and time using str method of datetime object: ")
print (str(now))

print
print ("Current date and time using instance attributes: " )
print ("Current year: ", now.year)
print ("Current month: ", now.month)
print ("Current day: ", now.day)
print ("Current hour: ", now.hour)
print ("Current minute: ", now.minute)
print ("Current second: ", now.second)
print ("Current microsecond: ", now.microsecond)

print
print ("Current date and time using strftime: ")
print (now.strftime("%Y-%m-%d %H:%M"))
