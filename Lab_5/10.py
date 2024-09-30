# Function to generate the first N Fibonacci numbers
def fibonacci(n):
    fibs = []
    a, b = 0, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs

# Specify the number of Fibonacci numbers to generate
N = 10

# Generate the first N Fibonacci numbers
fib_numbers = fibonacci(N)

# Use map to compute the square of each Fibonacci number
squared_fib_numbers = list(map(lambda x: x ** 2, fib_numbers))

# Print the results
print("First", N, "Fibonacci numbers:", fib_numbers)
print("Squares of the first", N, "Fibonacci numbers:", squared_fib_numbers)
