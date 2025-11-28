''' basic vale:
+     ------>adiition
-    ---->subtraction/negation
=--> assignment
/ --->float div
//-->floor div
* --->multipy
** -->square
% ----->mosulus
'''

print(
    5 + 2,      # addition → 7
    5 - 2,      # subtraction → 3
    -5,         # negation → -5
    5 / 2,      # float division → 2.5
    5 // 2,     # floor division → 2
    5 * 2,      # multiplication → 10
    5 ** 2,     # exponent → 25  ->5^2
    5 % 2,      # modulus → 1
    sep="\n"
)



# when we give sep argument to a print then it seprates each argument with that str


# Boolean examples
a = 10
b = 3

print(a > b)          # True
print(a < b)          # False
print(a == 10)        # True
print(a != b)         # True
print(a >= b)         # True
print(a <= b)         # False

x = True
y = False

print(x and y)        # False
print(x or y)         # True
print(not x)          # False


# String examples
s1 = "Hello"
s2 = "World"

print(s1 + " " + s2)      # concatenation → Hello World

star = "*"
print(star * 5)           # repetition → *****

print("H" in s1)          # True
print("z" not in s1)      # True



x = 10
x += 5     # x = x + 5
print(x)   # 15

x *= 2     # x = x * 2
print(x)   # 30

x %= 7     # x = x % 7
print(x)   # 2





a = 5     # 0101
b = 3     # 0011

print(a & b)   # AND  → 1
print(a | b)   # OR   → 7
print(a ^ b)   # XOR  → 6
print(~a)      # NOT  → -6
print(a << 1)  # left shift  → 10
print(a >> 1)  # right shift → 2

