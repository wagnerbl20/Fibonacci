# Define a function to calculate Fibonacci numbers
def fibonacci(n):
    # Initialize variables for the first two Fibonacci numbers
    fib = [0, 1]

    # Loop from the 3rd Fibonacci number up to the nth Fibonacci number
    for i in range(2, n):
        # Calculate the next Fibonacci number by adding the previous two numbers
        fib.append(fib[-1] + fib[-2])

    # Return the list of Fibonacci numbers
    return fib

# Calls the fibonacci function with argument x to get the Fibonacci numbers
x = int(input("Enter a number: "))
fibonacci_numbers = fibonacci(x)

# Print the Fibonacci numbers
print("Thee first", x , "Fibonacci numbers are:", fibonacci_numbers)
