# Student Management System

A Python-based Student Management System that allows users to manage student records through a simple Command Line Interface (CLI). The application supports CRUD operations (Create, Read, Update, Delete) and stores data permanently using a JSON file.

## Features

* Add Student Records
* View Total Number of Students
* View Student Names
* View Full Student Details
* Search Student by Roll Number
* Update Student Information
* Delete Student Records
* Persistent Data Storage using JSON
* Menu-Driven Interface
* Uses Python Match-Case Statements

## Technologies Used

* Python 3.10+
* JSON File Handling
* Dictionaries
* Functions
* Match-Case (Switch Case)

## Project Structure

```text
student-management-system/
│
├── main.py
├── students.json
└── README.md
```

## How It Works

### Add Student

Stores student details such as:

* Roll Number
* Name
* Course
* Email
* Phone Number

### View Students

Provides a submenu to:

1. View Total Students
2. View Student Names
3. View Full Details

### Search Student

Searches for a student using the Roll Number.

### Update Student

Updates existing student information.

### Delete Student

Removes a student record from the system.

### JSON Storage

Student data is saved in `students.json`, allowing records to remain available even after the program is closed.

## Sample JSON Data

```json
{
    "101": {
        "Name": "Rahul Sharma",
        "Course": "BCA",
        "Email": "rahul@gmail.com",
        "Phone": "9876543210"
    }
}
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/student-management-system.git
```

2. Navigate to the project directory:

```bash
cd student-management-system
```

3. Run the program:

```bash
python main.py
```

## Learning Outcomes

This project demonstrates:

* Python Programming Fundamentals
* Dictionaries and Nested Dictionaries
* Functions
* File Handling
* JSON Serialization and Deserialization
* CRUD Operations
* Match-Case Statements
* Menu-Driven Program Design

## Future Enhancements

* Password Authentication
* Student Marks Management
* CSV Export Feature
* GUI Version using Tkinter
* Database Integration (MySQL/SQLite)
* Report Generation

## Author

Sanskriti Gilda

## License

This project is open source and available for educational purposes.
