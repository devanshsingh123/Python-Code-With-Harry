import time

t = time.localtime().tm_hour

t1 = time.strftime('%H:%M:%S')
t2 = time.strftime('%H')
t3 = time.strftime('%M')
t4 = time.strftime('%S')

print(t1)
print(t2)
print(t3)
print(t4)

print(t)

if(t<12):
    print("Good Morning!")
elif(t>12 and t<=17):
    print("Good Afternoon!")
elif(t>17 and t<=21):
    print("Good Evening!")
else:
    print("Good Night!")    


 
 