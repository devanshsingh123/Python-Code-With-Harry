from functools import reduce

# old way of going about it 

def cube(x):
    return x*x*x


# l = [2,34,56,21,89,36]
# newl = []

# for item in l:
#     newl.append(cube(item))

# print(newl)


# NEW WAY USING MAP

# l = [2,34,56,21,89,36]

# cube = map(lambda x: x*x*x , l)


# cube = map(cube,l)

# print(list(cube))

# # FILTER

# def isEven(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
    
# is_even = filter(isEven,l)

# print(list(is_even))

# REDUCE

# def sum(x,y):
#     return x+y

l = [2,34,56,21,89,36]

#sumation = reduce(sum,l)

sum = reduce(lambda x,y: x+y,l)

print(sum)
