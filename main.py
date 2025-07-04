# Task 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n<= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print('Task 1')
print(fib(10))  
print(fib(15))  
print(' ')

#Task 2
import re
def generator_numbers(text: str):
    text_digits = re.findall(r' \d+\.\d+ | \d+ ', text) #space before and after numbers
    for num in text_digits:
        yield float(num)

def sum_profit(text: str, generator_numbers: callable) -> float:
    total = 0
    for number in generator_numbers(text):
        total += number
    return total

print('Task 2')
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
print(' ')