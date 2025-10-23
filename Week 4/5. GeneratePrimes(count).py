#Erya Anom

def generatePrimes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if isPrime(num):
            primes.append(num)
        num += 1
    return primes

# Example usage:
print(generatePrimes(10))
