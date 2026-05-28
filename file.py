with open("log.txt", "a") as file:
    file.write("Program run successfully\n")

with open("log.txt", "r") as file:
    logs = file.read()
    print(logs)