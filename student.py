students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")

        students.append([name, roll])
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent Records")

        for student in students:
            print("Name:", student[0], "| Roll No:", student[1])

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")