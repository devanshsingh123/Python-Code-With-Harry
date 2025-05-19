ep1 = {
    222:72,
    342:98,
    347:87,
    121:65,
    455:89
}

ep2 = {
    352:65,
    321:67,
    876:98
}

# print(ep1,ep2)

# Update method

ep1.update(ep2)
# print("Updated ep1: ", ep1)

# clear method
# print(ep2)
# ep2.clear()
# print(ep2)

#pop method
print(ep1)
ep1.pop(222) # removed element of key 222
print(ep1)

# pop item

ep1.popitem()
print(ep1) # removed the last element
