def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else None
def power(a, b): return a ** b
def square_root(a): return a ** 0.5
def absolute(a): return abs(a)
def factorial(n): import math; return math.factorial(n)
def gcd(a, b): import math; return math.gcd(a, b)
def lcm(a, b): import math; return (a * b) // math.gcd(a, b)
def is_prime(n): return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
def round_number(n, decimals=2): return round(n, decimals)
