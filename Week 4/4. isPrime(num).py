#Erya Anom


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # optimized check
        if num % i == 0:
            return False
    return True

# Example usage:
print(isPrime(7))   # True
print(isPrime(9))   # False
