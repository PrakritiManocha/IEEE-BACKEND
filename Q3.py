import math

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    gcd1 = math.gcd(num1, num2)
    gcd2 = math.gcd(num3, num4)
    gcd3 = math.gcd(gcd1, gcd2)
    gcd_final = math.gcd(gcd3, num5)
    print("The greatest common divisor of" , num1 , num2, num3, num4,"and" ,num5," is", gcd_final)

except ValueError:
    print("Invalid input. Please enter valid integers.")

