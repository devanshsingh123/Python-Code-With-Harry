
import requests


# def download_file(url,local_filename):
#     if local_filename is None:
#         local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
#     return local_filename


# parser = argparse.ArgumentParser(description="File Download CLI")

# parser.add_argument('url',help='URL of the file to Download')
# parser.add_argument('-o',"--output",type=str,help="Name with which file will be stored",default=None)

# args = parser.parse_args()


# print(args.url)
# print(args.output,type(args.output))
# download_file(args.url,args.output)

import argparse

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self, other):
        return self.num1 * self.num2

    def div(self, other):
        if other.value == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1/self.num2
    

parser = argparse.ArgumentParser(description="Calculator CLI")

parser.add_argument('num1',type=int,help='first digit')
parser.add_argument('num2',type=int,help='second digit')
parser.add_argument('-o',"--operation",type=str,help="What operation performed between both digits : add, subtract, multiply, or divide ")



args = parser.parse_args()
try:
    cal = Calculator(args.num1,args.num2)

    operation = args.operation

    if operation == 'add':
        print(f"Result:{cal.add()}")

    elif operation == "subtract":
        print(f"Result:{cal.sub()}")

    elif operation == "multiply":
        print(f"Result:{cal.mul()}")

    elif operation == "divide":
        print(f"Result:{cal.div()}")

    else:
        print("Please enter correct operation!")
except Exception as  ex:
    print(ex)


