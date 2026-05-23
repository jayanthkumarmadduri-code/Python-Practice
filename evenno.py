def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Even numbers between", a, "and", b, "are:")
print_even_numbers(a, b)