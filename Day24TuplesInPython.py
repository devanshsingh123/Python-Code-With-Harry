tup = (2,34,2,67,"Harry")
# assing single value with comma or else it will be taken as string
#Incorrect way
tup2 = (5)
#Correct way
tup3 = (5,)

print(type(tup))
print(type(tup2)) # not a tuple but a integer
print(type(tup3))
print(tup)
print(tup[0])
print(tup[-1])
print(tup[3])
print(tup[2])
print(tup[4])
print(len(tup))
print(tup[0:3])

if 34 in tup:
    print("Yes 34 is present")

# Tuple Operations
#
#  Tuple Concatenation

tuple1 = (1,2,3)
tuple2 = (4,5,6)

new_tuple = tuple1+tuple2

print(new_tuple)


#Tuple Repetition

repeat_tuple = ("Hello","Harry") * 3

print(repeat_tuple)

# Checking Membership

if "Harry" in repeat_tuple:
    print("Yes the string \'Harry\' exists in the tuple")


# Tuple Functions 

numbers = (10, 20, 30, 40, 50,20,20)

print(len(numbers))  # 5 (length of tuple)
print(max(numbers))  # 50 (largest value)
print(min(numbers))  # 10 (smallest value)
print(numbers.count(20)) # returns you the number of occurence of the value
print(sum(numbers))  # 150 (sum of elements)
print(numbers.index(20)) # gives you the index of the first occurence
print(numbers.index(20,3,7)) # Gives you value of index of the occurence in the mention sliced list . where 3 is considered and 7 is not considered as followed in slicing


# Converting Between Tuples and Lists
values_tuple = ("Harry","Devansh",2,34,12,54)

values_list = list(values_tuple) # now modification can be made on this copy of tuple as it is a list

print(type(values_tuple))
print(type(values_list))

#  Tuple Packing & Unpacking

person = ("Devansh",26,"Software Engineer")
l = list()
l = person 
name,age,designation = person
print(l)

print(name,", ",age,", ",designation)