# In below case the loop goes to its entire range and when the rage ends it goes to the sle loop

# for i in range(4):
#     print(i)

# else:
#     print("In the else loop")




# In below loop the for loop do not go its entire range and its broken and becaue of this else is not used

# for i in range(6):
#     print(i)
#     if i == 4:
#         break

# else:
#     print("sorry no i")


for i in range(6):
    if i== 3:
        continue
    print (i)
else:
    print("In else")