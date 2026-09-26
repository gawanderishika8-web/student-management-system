# student-management-system
About the Project

I created this Student Management System using Python to practice programming by building something that can actually be used to manage basic student information.

The program stores details such as Roll Number, Name, Branch, Marks, and Grade. Instead of keeping all the operations in separate programs, I combined them into one menu-driven application where the user can perform different operations according to their requirement.

I also added some validation and statistical features so that the project is not limited to simply storing and displaying student data.

What Can This Project Do?

The program provides the following options:

1. Add Student

A user can enter a student's Roll Number, Name, Branch, and Marks.

Before adding the record, the program checks whether the Roll Number already exists. It also checks that marks are within the valid range of 0 to 100.

2. View Students

This option displays all the students currently stored in the program along with their:

- Roll Number
- Name
- Branch
- Marks
- Grade

3. Search Student

A student can be searched using their Roll Number.

If the Roll Number exists, the program displays the student's information. Otherwise, it shows a student-not-found message.

4. Search by Branch

The program can also find students belonging to a particular branch.

The search is case-insensitive, so entering "ece" or "ECE" will give the same result.

5. Update Student

The user can update an existing student's:

- Name
- Branch
- Marks

Whenever the marks are changed, the student's grade is calculated again automatically.

6. Delete Student

A student record can be removed using the Roll Number.

7. Student Statistics

This is one of the main features I added to the project.

It calculates:

- Total number of students
- Average marks
- Number of passed students
- Number of failed students
- Highest-scoring student's name
- Highest marks

The topper is determined automatically by comparing the marks of all stored students.

Grade Calculation

The program automatically assigns a grade according to the marks:

Marks| Grade
90–100| A+
80–89| A
70–79| B
60–69| C
50–59| D
Below 50| F

The grade is calculated using a separate "get_grade()" function, which keeps the grading logic organized and reusable.

Python Concepts Used

While making this project, I worked with several Python concepts:

- Functions
- "if-elif-else"
- "for" loops
- "while" loops
- Lists
- Dictionaries
- User input
- String methods
- Searching
- Updating and deleting data
- Basic calculations
- Input validation
- Menu-driven programming

The student records are stored using a list of dictionaries, which makes it possible to keep multiple students and access individual information using keys such as "roll", "name", "branch", "marks", and "grade".

How the Program Works

The program starts with a menu containing different operations.

The user selects an option by entering its number. The corresponding function is then called to perform that operation.

The program continues running until the user selects Exit.

===================================
      STUDENT MANAGEMENT SYSTEM
===================================
1. Add Student
2. View Students
3. Search Student
4. Search by Branch
5. Update Student
6. Delete Student
7. Student Statistics
8. Exit
===================================

Example

Enter Roll No: 101
Enter Name: Rishika
Enter Branch: ECE
Enter Marks: 95

Student added successfully!

The program automatically calculates:

Grade: A+

If the same Roll Number is entered again, the program prevents the duplicate record.

Running the Project

This is a command-line Python project and does not require any external libraries.

Run the project using:
project.py

The program will open directly in the terminal.

Project Structure

student-management-system/
│
├── project.py
└── README.md

Future Improvements

I would like to improve this project further by adding permanent data storage using files or a database. A login system, graphical interface, and more detailed student reports could also be added in future versions.

Author

Rishika Gawande

This project was created to strengthen my Python programming fundamentals and understand how individual concepts can be combined to build a complete working application.
