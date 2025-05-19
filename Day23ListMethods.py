
l = [11,62,83,14,85]
l1 = [["Zander","Devansh"],["Ravi"],["Race"]]
l2 = ["Xavier","Helo","Swan","Lot"]
l3 = ["@","$","*"]

# Use of sort method, it seems it only wroks on similar data type

l1.sort()
l2.sort()
l3.sort()
print(l1)
print(l)
print(l2)
print(l3)

# Reversin the list using sort
# l.sort(reverse="True")

# reverse Method

l.reverse()
print(l)


# Add the value in the end 

l.append(22)
print(l)

# Add the element at a certain index

l.insert(3,"Devansh")
print(l)

# Lets try to insert it at an index that is bigger then the list

l.insert(-9,"Hello")
print(l)

print(len(l))

# Removing elements
  
# Remove first occurrence of value.

# Raises ValueError if the value is not present.
l.remove(83)
print(l)

# Using pop

# removes the last element

l.pop()
print(l)

# can remove value from mentioned  index  

l.pop(0)
print(l)

# Using del

del l[1]
print(l)

# Updating elements

l[3] = 24
print(l)


# Iterating Over Lists

Names = ["Devansh","Ravi","Sahil","Ishaan"]

for name in Names:
    print(name)

# Using enumerator to get index and value

for index,name in enumerate(Names):
    print(index,": ",name)

# Using List Comprehension 
numbers = [12,15,32,67,45,66,29]
squared = [num ** 2 for num in numbers]

print(squared)

#  Checking for Membership

print("Sahil" in Names)

print("Inder" not in Names)


# List Functions

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))