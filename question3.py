#Write a program that takes an integer as input and returns true if the input is a power of two.
import math

def is_power_of_two(num):
    result= math.log2(num)
    return result.is_integer()

try:
    print("enter the number you wish to check if it is a power of 2\n")
    num=int(input(">> "))
except Exception as e:
    print("Enter a valid number\n")
    exit()

print(f'Is a power of 2: {is_power_of_two(num)}')