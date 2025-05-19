# readlines() method
# The readline() method reads a single line from the file. 
# If we want to read multiple lines, we can use a loop.

# Reading using readline

f = open('myfile1.txt','r')
i=0
while True:
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])  
    print(f"Marks of Maths of Student {i+1} is: {m1}")
    print(f"Marks of Physics of Student {i+1} is: {m2}")
    print(f"Marks of Chemistry of Student {i+1} is: {m3}")
    i+=1
    print(line)
    

# while True:
#     line = f.readline()
#     if not line :
#         break
#     print(line)



# The readlines() method reads all the lines of the file 
# and returns them as a list of strings.

# writelines() method

# The writelines() method in Python writes a sequence of strings to a file.
# The sequence can be any iterable object, such as a list or a tuple.

# Here's an example of how to use the writelines() method:

f = open('myfile.txt','w')

# lines = ['line1\n','line2\n','line3\n','line4\n','line5\n']

# f.writelines(lines)
# f.close()

# lines = ['line 1','line 2','line 3','line 4']

# for line in lines:
#     f.write(line + '\n')

# f.close()