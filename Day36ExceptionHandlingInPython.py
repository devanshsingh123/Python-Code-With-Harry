# a = input("Enter a number: ")
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{a} X {i} = {int(a)*(i)}")
# except:
#     print("Invalid Input!")







try:
    num = int(input("Enter a number: "))
    a = [2,6]
    print(a[num])
except ValueError as valerr:
    print(valerr)
except IndexError as ierr:
    print(ierr)


print("Some lines of code")
print("end of program")