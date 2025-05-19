dict = {
    "Devansh" : "Human",
    "Spoon" : "Object"
}

# print(dict)

# print(dict["Devansh"]) # If the key do not exixts this will throw error

# print(dict.get("Spoon")) # If the key do not exists this will return None

# for key in dict.keys():
#     print(f"The value in key {key} is :  {dict[key]}")

print(dict.items())

for key,value in dict.items():
    print(f"The value in key {key} is : {value}")