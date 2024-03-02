# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci(limit):
    a=0
    b=1

    fibonacci_seq=[]

    while a<limit:
        fibonacci_seq.append(a)
        #determine the next fibonacci_seq number to the array
        c=a
        a=b
        b=c+b


    return fibonacci_seq

limit=100

result=fibonacci(100)
print(f'results: {result}')

