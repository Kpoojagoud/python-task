#basic input with integer conversion take 2 num input user convert them to integer 
a = int(input('Enter:')) 
b = int(input('Enter:')) 
print(a+b) 

#Multiple Inputs with Space Separation Take two floating-point numbers as input in a single line separated by space and print their product 
a, b = map(float, input("Enter numbers separated by space: ").split())
c = a * b 
print(c) 

#	Expression Evaluation with eval()Take a mathematical expression from the user as input and print the evaluated result.
a =input('Enter Expression:') 
b = eval(a)
print(b) 

#List Input using eval()take a list as input using eval() and print the sum of its elements. 
a= eval(input('enter:'))
b = 0
for i in a :
    b = b+i 
print(b) 

#Boolean Type ConversionTake an input from the user, convert it to boolean, and print the result. 
a = bool(input('enter:'))
print(a)  

#	String to Float ConversionTake a floating-point number as string input, convert it to float, and print its square.
a = input('enter:') 
b = float(a) 
print(b**b)  

# Dictionary Input using eval()Take a dictionary as input using eval() and print its keys and values separately
a = input('enter:')
b = eval(a)    
print("Keys:", list(b.keys()))
print("values:", list(b.values()))

#List of Integers from Space Separated Input Take a list of integers as input in a single line separated by space and print the maximum and minimum values.
a = list(input('enter numbers by space:').split())
print(min(a))
print(max(a)) 

#Mixed Type Literal Input with eval()Take any Python literal as input (string, list, tuple, int, etc.) using eval() and print its type.
a = eval(input('enter:'))
print(type(a)) 

#Combined Type ConversionTake two inputs, convert the first to integer and second to float, then print their sum. 
a = int(input('enter:'))
b = float(input('enter:')) 
print(a+b)




