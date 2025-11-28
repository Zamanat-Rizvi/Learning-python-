
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
#Sum till n terms
elif inp == "Sum-n":
    num1 = int(input("Enter the value of n "))
    print((num1*(num1-1))/2)
else :
    print("invalid input!")
