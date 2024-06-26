# without recursion
def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        n = n // 10
    return sum_digits


print(sum_of_digits(123456))
