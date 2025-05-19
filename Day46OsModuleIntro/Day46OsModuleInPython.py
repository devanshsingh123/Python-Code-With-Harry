import os

#Checking if folder exists or not
if( not os.path.exists("data")):
    os.mkdir("data")

# Create  folders
# for i  in range(0,100):
#     os.mkdir(f"data/Day{i+1}")

# Rename the existing folders 
# for i  in range(0,100):
#     os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")

# Get the list of folders present in directory

folders = os.listdir("data")

print(os.getcwd())

# print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))