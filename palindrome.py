# Function to check palindrome
def is_palindrome(text):

    reversed_text = ""

    # Reversing the string using a loop
    for char in text:
        reversed_text = char + reversed_text

    # Checking if original and reversed strings are same
    if text == reversed_text:
        return True
    else:
        return False


# Taking input from the user
string = input("Enter a string: ")

# Calling the function
if is_palindrome(string):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")