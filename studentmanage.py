import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("Total Students:", len(students))

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                roll = input("Enter Roll No: ")

                if roll in students:
                    print("Roll Number already exists!")
                else:
                    name = input("Enter Name: ")
                    course = input("Enter Course: ")
                    email = input("Enter Email: ")
                    phone = input("Enter Phone Number: ")

                    students[roll] = {
                        "Name": name,
                        "Course": course,
                        "Email": email,
                        "Phone": phone
                    }

                    save_students(students)
                    print("Student Added!")

            case "2":
                if not students:
                    print("No student found!")
                else:
                    while True:
                        print("\n--- View Menu ---")
                        print("1. View Total Students")
                        print("2. View Student Names")
                        print("3. View Full Details")
                        print("4. Back")

                        view_choice = input("Enter your choice: ")

                        match view_choice:

                            case "1":
                                print("Total Students:", len(students))

                            case "2":
                                print("\nStudent Names:")
                                for roll, data in students.items():
                                    print("-", data["Name"])

                            case "3":
                                print("\nFull Details:")
                                for roll, data in students.items():
                                    print("\nRoll No:", roll)
                                    print("Name:", data["Name"])
                                    print("Course:", data["Course"])
                                    print("Email:", data["Email"])
                                    print("Phone:", data["Phone"])

                            case "4":
                                break

                            case _:
                                print("Invalid Choice!")

            case "3":
                roll = input("Enter Roll No to Search: ")

                if roll in students:
                    print("\nStudent Found")
                    print("Roll No:", roll)
                    print("Name:", students[roll]["Name"])
                    print("Course:", students[roll]["Course"])
                    print("Email:", students[roll]["Email"])
                    print("Phone:", students[roll]["Phone"])
                else:
                    print("Student Not Found!")

            case "4":
                roll = input("Enter Roll No to Update: ")

                if roll in students:
                    students[roll]["Name"] = input("Enter New Name: ")
                    students[roll]["Course"] = input("Enter New Course: ")
                    students[roll]["Email"] = input("Enter New Email: ")
                    students[roll]["Phone"] = input("Enter New Phone Number: ")

                    save_students(students)
                    print("Student Updated!")
                else:
                    print("Student Not Found!")

            case "5":
                roll = input("Enter Roll No to Delete: ")

                if roll in students:
                    del students[roll]
                    save_students(students)
                    print("Student Deleted!")
                else:
                    print("Student Not Found!")

            case "6":
                print("Program Exited.")
                break

            case _:
                print("Invalid Choice!")


main()
