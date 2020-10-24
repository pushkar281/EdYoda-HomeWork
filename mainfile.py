from calculator import *

a = int(input("Enter 'a' value: "))
b = int(input("Enter 'b' value: "))

print(f"Sum is {arithmetic.addition(a,b)}")
print(f"Difference is {arithmetic.subtraction(a,b)}")
print(f"Product is {arithmetic.multiplication(a,b)}")
print(f"True division is {arithmetic.truedivision(a,b)}")
print(f"The quotient is {arithmetic.division(a,b)[0]} and remainder is {arithmetic.division(a,b)[1]}")

print(f"The square of a is {scientific.square(a)}")
print(f"The cube of a is {scientific.cube(a)}")
print(f"The value of a to the power b is {scientific.custom(a,b)}")

print(f"The value of pi is : {logical.pi()}")


