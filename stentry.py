students = {}

while True:

    print("\nMENU")
    print("A - Add a Student")
    print("B - Update Marks")
    print("C - Search for a Student")
    print("D - Display All Students and Marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()


    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully")


    elif choice == 'B':
        name = input("Enter student name to update: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully")
        else:
            print("Student not found")


    elif choice == 'C':
        name = input("Enter student name to search: ")

        if name in students:
            print(name, "has", students[name], "marks")
        else:
            print("Student not found")


    elif choice == 'D':
        print("\nStudent Records:")

        if len(students) == 0:
            print("No records found")
        else:
            for name, marks in students.items():
                print(name, ":", marks)


    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice")