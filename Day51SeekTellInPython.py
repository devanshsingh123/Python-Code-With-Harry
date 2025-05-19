# with open('myfile.txt','r') as f:
#     print(f.tell())


#     # Move to the 10th byte in the file
#     f.seek(10)
#     position1 = f.tell()

#     data = f.read(5)
#     position2 = f.tell()
#     print(data,position1,position2)

def build_customer_index(filename):
    # Dictionary to store our index
    customer_index = {}
    
    # Open and read the file line by line
    with open(filename, 'r') as file:
        while True:
            # Remember the current position before reading the line
            position = file.tell()
            
            # Read the next line
            line = file.readline()
            
            # If we've reached the end of file, stop
            if not line:
                break
                
            # Parse the line to get the customer ID (assuming it's the first field)
            customer_id = line.split(',')[0]
            
            # Store the position in our index, using customer ID as the key
            customer_index[customer_id] = position
    
    # Return the completed index
    return customer_index

# Save the index to use later
index = build_customer_index('clientSheet.txt')

def find_customer(filename, customer_id, index):
    # Check if the customer ID exists in our index
    if customer_id not in index:
        return "Customer not found"
    
    # Open the file and seek to the position from our index
    with open(filename, 'r') as file:
        file.seek(index[customer_id])
        
        # Read and return the customer record
        return file.readline().strip()

# Find customer 1002
customer_data = find_customer('customers.txt', '1002', index)
print(customer_data) 


    
     