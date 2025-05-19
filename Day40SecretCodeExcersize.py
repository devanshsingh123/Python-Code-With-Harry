# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import string
import random

#generating the random string

def genrateRandomString(len):
    char = string.ascii_letters
    return ''.join(random.choices(char,k=len))


    

def code(words):
    nwords = []
    for word in words:
        if(len(word)>=3):
            #coding with standard rule regarding
            coded_str = f"{genrateRandomString(3)}{word[1:len(word)]}{genrateRandomString(3)}{word[0:1]}"
            nwords.append(coded_str)
        else:
            #just reversing the str
            coded_str = str[::-1]
            nwords.append(coded_str)
    print(" ".join(nwords))
    
def decode(words):
    nwords = []
    for word in words:
        if(len(word)>=3):
            #code logic
            decoded_str = f"{word[-1:]}{word[3:len(word)-4]}"
            nwords.append(decoded_str)
        else:
            decoded_str = word[::-1]
            nwords.append(decoded_str)
    print(" ".join(nwords))


# str = 'aghtjjytyujikgA'
# print(str[3:len(str)-4])

option = int(input("Enter \'1\' for code and \'2\' for decode :"))
str = input("Please insert the string: ")
words = str.split(" ")


if(option == 1):
    code(words)
else:
    decode(words)
 
