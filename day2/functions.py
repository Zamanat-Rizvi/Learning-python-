

def add(a:int=0,b:int=0,c=0,d=0,e=0,f=0,g=0,h=0)->float:
    '''this function returns the sum of numbers'''
    return a+b+c+d+e+f+g+h

print(add(1,2,2))
print(add.__doc__)

def play():
    pass

def sum(*args:float)->float:
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(1,2,3,4,5,6,7,8,9,10))


# lambda argument:return value
inverse=lambda x:(1/x)
print(inverse(0.5))

# to understand recursion u must know what is recursion
# x!=x.(x-1)!
def factorial(n:int):
    # break point
    return 1 if n==0 else n*factorial(n-1)
print(factorial(995))



# make a function to find sum of n natural number 
# s(n)=n+s(n-1)
