def absolute(x):
    return x if x >= 0 else -x

def floor(x):   
    int_x = int(x)
    return int_x if x >= 0 or int_x == x else int_x - 1

def ceil(x):
    int_x = int(x)
    return int_x if x <= 0 or int_x == x else int_x + 1

def GCD(a, b):
    while b:
        a, b = b, a % b        
    return a

def LCM(a, b):
    return abs(a * b) // GCD(a, b)  

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#print("This is file1.py in mathsinpython package")
#print("Absolute of -5 is:", absolute(-5))
#print("Floor of 3.7 is:", floor(3.7))
#print("Ceil of 3.2 is:", ceil(3.2))
#print("GCD of 48 and 18 is:", GCD(48, 18))
#print("LCM of 4 and 6 is:", LCM(4, 6))
#print("2 to the power 10 is:", power(2, 10))
#print("First 10 Fibonacci numbers:", fibonacci(10))
#print("Is 29 a prime number?", isPrime(29))
#print("Factorial of 5 is:", factorial(5))

def __init__():
    print("mathsinpython.basicmaths module initialized")