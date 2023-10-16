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