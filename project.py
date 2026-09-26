# Student Management System

students = []


def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def add_student():
    roll = input("Enter Roll No: ")

    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100!")
        return

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks,
        "grade": get_grade(marks)
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records available.")
        return

    print("\n--- STUDENT RECORDS ---")

    for s in students:
        print("Roll No :", s["roll"])
        print("Name    :", s["name"])
        print("Branch  :", s["branch"])
        print("Marks   :", s["marks"])
        print("Grade   :", s["grade"])
        print("-" * 30)


def search_student():
    roll = input("Enter Roll No to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found!")
            print("Name   :", s["name"])
            print("Branch :", s["branch"])
            print("Marks  :", s["marks"])
            print("Grade  :", s["grade"])
            return

    print("Student not found!")


def search_by_branch():
    branch = input("Enter Branch: ")
    found = False

    for s in students:
        if s["branch"].lower() == branch.lower():
            print(
                s["roll"], "|",
                s["name"], "|",
                s["marks"], "|",
                s["grade"]
            )
            found = True

    if not found:
        print("No student found in this branch.")


def update_student():
    roll = input("Enter Roll No: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["branch"] = input("Enter New Branch: ")

            marks = float(input("Enter New Marks: "))

            if marks < 0 or marks > 100:
                print("Invalid marks!")
                return

            s["marks"] = marks
            s["grade"] = get_grade(marks)

            print("Student record updated!")
            return

    print("Student not found!")


def delete_student():
    roll = input("Enter Roll No: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student record deleted!")
            return

    print("Student not found!")


def show_statistics():
    if len(students) == 0:
        print("No records available.")
        return

    total = len(students)
    total_marks = 0
    passed = 0
    failed = 0
    highest = students[0]

    for s in students:
        total_marks += s["marks"]

        if s["marks"] >= 50:
            passed += 1
        else:
            failed += 1

        if s["marks"] > highest["marks"]:
            highest = s

    average = total_marks / total

    print("\n--- STUDENT STATISTICS ---")
    print("Total Students :", total)
    print("Average Marks  :", round(average, 2))
    print("Passed         :", passed)
    print("Failed         :", failed)
    print("Topper         :", highest["name"])
    print("Topper Marks   :", highest["marks"])


# Main Program

# Main Program

while True:
    print("\n===================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Search by Branch")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Student Statistics")
    print("8. Exit")
    print("====================================")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        search_by_branch()
    elif choice=="5":
        update_student()
    elif choice=="6":
        delete_student()
    elif choice=="7":
        show_statistics()
    elif choice=="8":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice! Please try again.")

    