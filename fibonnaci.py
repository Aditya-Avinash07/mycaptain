def fibonacci_numbers(limit):
    fib_list = [0, 1]
    while True:
        next_num = fib_list[-1] + fib_list[-2]
        if next_num <= limit:
            fib_list.append(next_num)
        else:
            break
    return fib_list

# Input: The limit up to which you want to generate Fibonacci numbers
limit = int(input("Enter the limit for Fibonacci numbers: "))
fib_sequence = fibonacci_numbers(limit)
print("Fibonacci numbers up to", limit, ":", fib_sequence)
