"""A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.

https://py.checkio.org/en/mission/perfect-number-checking/"""


def is_perfect(n: int) -> bool:
    if n < 6: 
        return False
    
    sum_divisors = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
