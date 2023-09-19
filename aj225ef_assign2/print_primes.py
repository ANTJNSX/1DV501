
primes = []

def generate_primes(count):
    num = 2
    while len(primes) < count:
        is_prime = True

        for p in primes:
            if num % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
        num += 1


n = int(input("input the amount of prime numbers you want to print: "))

generate_primes(n)


count=0
for i in range(0,len(primes)):
    print(primes[i], end=" ")
    count+=1

    if count==10:
        print('\n', end="" )
        count=0
