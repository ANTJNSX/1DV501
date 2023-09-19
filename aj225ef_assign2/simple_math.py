
def inc(n):           #  Increments n with one
    return n+1

def inc_with(n, t):   #  Increments n with the value of t
    return n+t    

def greatest(n1, n2): #  Returns the largest of the values n1 and n2
    return n1 if n1>n2 else n2

def is_even(n):       #  Returns True if n is even, otherwise false
    return True if n%2==0 else False

def power(x, n):      #  Returns x to the power of n
    return x**n

def factorial(n):     #  Returns the factorial of n
    s=1
    for i in range(1,n+1):
        s*=i
    return s

def is_prime(n):      #  Returns True if n is a prime, otherwise false
    for j in range(1,n):
        if n%j==0 and j!=n and j!=1:
            return False
    
    return True


print('41 plus 1:', inc(41))
print('30 plus 12:', inc_with(30, 12))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 10:', power(2, 10))

print('Factorial of 5:', factorial(5))

print('Is 41 a prime?:', is_prime(41))

