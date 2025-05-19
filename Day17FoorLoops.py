# name = "Devansh"

# for char in name:
#     print(char,end=", ")

# print(end="\n")    

# for i in range(0,len(name),2):
#     print(name[i],end=", ")

# print(end="\n")

# for i in range(5):
#     print(i,end=", ")

# print(end="\n")

# for i  in range(10,-1,-1):
#     print(i,end=", ")    


# print(end="\n")

# count =1

# while count <= 5:
#     print(count,end=", ")
#     count+=1


# # Use of break and continue in loops


# for i in range(8):
#     print(i)
#     if i == 6:
#         break


# for i in range(8):
#     if i>2 and i<6:
#         continue
#     print(i)  

# # Same use in While loop 
# for i in range(2, 51):  # Loop through numbers 2 to 50
#     isPrime = True  # Reset isPrime for each number

#     for j in range(2, int(i ** 0.5) + 1):  # Check divisibility from 2 to sqrt(i)
#         if i % j == 0:  # If divisible, it's not prime
#             isPrime = False
#             break  # No need to check further

#     if isPrime:
#         print(i)  # Print only if the number is prime

# import random

# random_number = random.randint(1, 100)  # Generates a random number between 1 and 100

# number = int(input("Guess the number: "))

# while number != random_number:
#     if(number > random_number):
#         print("You guessed wrong, the number is less than ",number)
#         number = int(input("Guess the number again: "))
#         continue
#     elif number < random_number:
#         print("You guessed wrong, the number is greater than ",number)
#         number = int(input("Guess the number again: "))
#         continue

# print("Congratulations you guessed correct. Hurray!") 
#   
#Optimum Code

import random

random_number = random.randint(1, 100)  # Generate random number between 1 and 100

while True:  # Infinite loop, breaks when correct guess is made
    try:
        number = int(input("Guess the number: "))  # Get user input

        if number > random_number:
            print("You guessed wrong, the number is LESS than", number)
        elif number < random_number:
            print("You guessed wrong, the number is GREATER than", number)
        else:
            print("🎉 Congratulations! You guessed it right. Hurray! 🎉")
            break  # Exit loop if guess is correct

    except ValueError:
        print("⚠️ Please enter a valid number!")  # Handle invalid inputs

    

    
