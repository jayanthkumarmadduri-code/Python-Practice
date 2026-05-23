print("----NUMBER GUESSING GAME----")
secret_number = 76
guess = int(input("Guess the number: "))
if guess > secret_number:
    print("Too high")
elif guess < secret_number:
    print("Too low")
else:
    print("Correct!")