class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

students = []

while True:
    print("===== Student Management System =========")

    print("\n 1. Add Student")
    print("2. View Student")
    print("3. Update Marks")
    print("4. Delete Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice  :  "))
    except ValueError:
        print("Enter a valid number")
        continue

    if choice == 5:
        break

    elif choice == 1:
        name = input("Enter your name  : ")
        try:
            roll_number = int(input("Enter your roll number  : "))
            marks = int(input("Enter your mark : "))
        except ValueError:
            print("Enter a valid number ")
            continue

        duplicate = False

        for student in students:
            if student.roll_number == roll_number:
                duplicate = True
                break

        if duplicate:
            print("Roll Number already exists")
            continue



        if 0 <= marks <= 100:
            student = Student(name, roll_number, marks)
            students.append(student)
            print("Student added successfully")
        else:
            print("Invalid Marks")

    elif choice == 2:
        if len(students) == 0:
            print("Students not found!!")
        else:
            try:
                roll_number = int(input("Enter your roll number : "))
            except ValueError:
                print("Enter a valid number")
                continue

            found = False

            for student in students:
                if student.roll_number == roll_number:
                    found = True
                    print("Name :", student.name)
                    print("Roll Number :", student.roll_number)
                    print("Marks :", student.marks)
                    print("-----------------------------")
                    break

            if not found:
                print("Student not found")



    elif choice == 3:
        try:
            search_roll = int(input("Enter your roll number  : "))

        except ValueError:
            print("Enter a valid number")
            continue

        found = False

        for student in students:
            if student.roll_number == search_roll:
                found = True
                print("name :", student.name)
                print("Current marks :", student.marks)

                try:
                    new_marks = int(input("Enter new mark :"))
                except ValueError:
                    print("Enter valid number")
                    continue

                if 0 <= new_marks <= 100:
                    student.marks = new_marks
                    print(new_marks)
                    print("Mark updated successfully!!!")
                    break
                else:
                    print("invalid marks")

        if not found:
            print("Student not found")


    elif choice == 4:
        try:
            search_student = int(input("Enter your ROll Number : "))
        except ValueError:
            print("Enter a valid number")
            continue

        found = False

        for student in students:
            if student.roll_number == search_student:
                found = True

                print("Name:  ", student.name)

                students.remove(student)

                print("Success...!")
                break

        if not found :
            print("Student not found!")