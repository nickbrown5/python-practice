
# function to get prime factors of a number
def get_prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors
