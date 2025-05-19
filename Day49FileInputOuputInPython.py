
# Character	: Meaning
# 'r'	       open for reading (default)
# 'w'	       open for writing, truncating the file first
# 'x'	       create a new file and open it for writing
# 'a'	       open for writing, appending to the end of the file if it exists
# 'b'	       binary mode
# 't'	       text mode (default)
# '+'	       open a disk file for updating (reading and writing)

# use 'rb' to acess a jpg , pdg , jpeg file

# READING A FILE

# f = open('myfile.txt','r')
# text = f.read()
# print(text)

# WRITING A FILE

# f = open('myfile.txt','w') # here using w will overright the exixting text
# f = open('myfile.txt','a') # will not overright but just add the string
# f.write("Hello I am trying to overide!")
# f.close()


# Here using with we do not need to close , it is already handled
with open('myfile.txt','a') as f:
  f.write("hey i am using with")