while True:

    
    n = input("Enter a number (or type 'Quit' to stop): ")

    
    if n.lower() == "quit":
        print("Program terminated")
        break

    
    n = float(n)

    
    if n > 0:
        print("Positive Number")

    elif n < 0:
        print("Negative Number")

    else:
        print("Zero")