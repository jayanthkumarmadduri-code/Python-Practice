numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


even_numbers = ()

for num in numbers:
    if num % 2 == 0:
        even_numbers = even_numbers + (num,)


odd_numbers = ()

for num in numbers:
    if num % 2 != 0:
        odd_numbers = odd_numbers + (num,)


print("Original Tuple :", numbers)
print("Even Numbers Tuple :", even_numbers)
print("Odd Numbers Tuple :", odd_numbers)