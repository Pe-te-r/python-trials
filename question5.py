'''
Write a program that takes an integer as input and returns an integer with reversed digit
ordering. '''

def reverse_number(number):
    reversed=str(number)[::-1]

    if number<0:
        reversed= "-"+reversed[:-1]
    

    return reversed

try:
    print("Enter the number you wish to revese\n")
    number=int(input(">> "))
    print(f'The reversed result is: {reverse_number(number)}')
    print()
except Exception as e:
    print("Enter a valid number\n")
