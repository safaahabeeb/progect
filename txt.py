students = []

def add():

    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    student_age = input("Student Age: ")

    student = {
        "id": student_id,
        "name": student_name,
        "age": student_age
    }

    students.append(student)
    print("Student added successfully!")

def display():
    if len(students) == 0:
        print("No students registered.")
    else:
        for student in students:
            print(f"Student ID: {student['id']}")
            print(f"Student Name: {student['name']}")
            print(f"Student Age: {student['age']}")
            print("--------------------")

def delete():
    student_id = input("Enter the student ID to delete: ")
    found = False

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            found = True
            break

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")
