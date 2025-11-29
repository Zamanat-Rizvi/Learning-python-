
#Calculator
print("Calculator!")
inp = input("Which operation do you like to do?(enter +,-,*,/,**,fact,Sum-n) ")

# Arithimatics
if inp == "+":
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    print(num1+num2)
    
elif inp == "-":
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    print(num1-num2)
    
elif inp == "*":
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    print(num1*num2)
    
elif inp == "/":
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    print(num1/num2)
    
# Exponentiation
elif inp == "**":
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    print(num1**num2)
    

#Recursion
elif inp == "fact":
    num1 = int(input("Enter a number "))
    def fact(n):
        #Factorial calculator
        return 1 if n == 0 else n * fact(n-1)
    print(fact(num1))
    
#Retry here
elif inp == "Sum-n":
    num1 = int(input("Enter the value of n "))
    def Sumn(n):
        #Sum n function
        return 0 if n==0 else n+Sumn(n-1)
    print(Sumn(num1))
else :
    print("invalid input!")  
    
# make it using recusrsion :
#Sum till n terms
# elif inp == "Sum-n":
#     num1 = int(input("Enter the value of n "))
#     print((num1*(num1-1))/2)
# else :
#     print("invalid input!")



# make all the operations function driven
# make the Sum-n recursive instead of using formula
# use match case instead of elif ladders
# add proper comments to specify what u did 
# btw current Sum-n is giving wrong output
