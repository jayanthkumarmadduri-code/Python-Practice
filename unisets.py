text = input("Enter a string: ")
unique_chars = set(text)
print("Unique characters are:")
for char in unique_chars:
    print(char)
print("Count of unique characters =", len(unique_chars))