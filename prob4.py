m=int(input('m= '))
n=int(input('n= '))

def factorial(x):
    factor=1
    for i in range(1, x-1):
        factor=factor*1
    return factor
print(factorial(n)/factorial(m)*factorial(n-m))