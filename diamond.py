n = 21

for i in range(n):
    spaces = abs(n//2 - i)
    nums = n - 2 * spaces
    print(" " * spaces + "01" * (nums//2) + ("0" if nums % 2 else ""))
