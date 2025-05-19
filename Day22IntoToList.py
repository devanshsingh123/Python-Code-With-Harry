marks = [1,2,4,"Devansh",{"Dev",2,3,4}]
# print(marks)
# print(type(marks))

# print(marks[2])

# print(marks[-3]) #Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3])
# print(marks[2])


# if "Devansh" in marks:
#     print("Yes")
# else:
#     print("No")


# # Same thing applies for string as well 
# if "arry" in "Harry":
#     print("Yes")
# else:
#     print("No")
        

print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:4:2])

# List Comprehension

lst = [i for i in range(4)]
print(lst)

lst1 = [i for i in range(10) if i%2 == 0]
print(lst1)
