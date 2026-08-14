ALL_STUDENTS = []


def Add_student():
    student_id = int(input("Enter Student ID : "))
    student_name = input("Enter Student Name : ")

    marks = []

    for i in range(3):
        mark = int(input(f"Enter Subject {i + 1} Marks : "))
        marks.append(mark)

    student = {
        "ID": student_id,
        "Name": student_name,
        "Marks": marks
    }

    ALL_STUDENTS.append(student)
    print()

    print("Student Added successfully")
    print()


def Display_students():

    if len(ALL_STUDENTS) == 0:
        print("No student Available ")
        return

    print("Present Students : ")

    for i in range(len(ALL_STUDENTS)):
        print(ALL_STUDENTS[i])


def Search_student():

    if len(ALL_STUDENTS) == 0:
        print("No student is present")
        return

    search_ID = int(input("Enter student ID : "))

    for i in range(len(ALL_STUDENTS)):

        if ALL_STUDENTS[i]["ID"] == search_ID:
            print(ALL_STUDENTS[i])
            return

    print("student is Not found")


def Update_student():

    if len(ALL_STUDENTS) == 0:
        print("No student available")
        return

    Search_ID = int(input("Enter Student ID : "))

    for i in range(len(ALL_STUDENTS)):
        if ALL_STUDENTS[i]['ID'] == Search_ID:

            ALL_STUDENTS[i]['Name'] = input("Enter Name to Update : ")

            marks = []

            for j in range(3):
                mark = int(input(f"Enter Subject {j + 1} marks : "))
                marks.append(mark)

            ALL_STUDENTS[i]['Marks'] = marks

            print("Updated sucessfully")
            return

    print("Student no found")


def Delete_student():

    if len(ALL_STUDENTS) == 0:
        print('No Student is vailable')
        return

    search_id = int(input("Enter student ID : "))

    for i in range(len(ALL_STUDENTS)):
        if ALL_STUDENTS[i]['ID'] == search_id:
            ALL_STUDENTS.pop(i)
            print("Deleted Successfully")
            return

    print("Student is not found")


def student_Result():

    if len(ALL_STUDENTS) == 0:
        print("No student is available")
        return

    search_id = int(input("Enter student ID "))

    for i in range(len(ALL_STUDENTS)):
        if ALL_STUDENTS[i]['ID'] == search_id:

            total_marks = 0

            for j in range(len(ALL_STUDENTS[i]["Marks"])):
                total_marks += ALL_STUDENTS[i]["Marks"][j]

            average = total_marks / len(ALL_STUDENTS[i]["Marks"])

            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            elif average >= 60:
                grade = "D"
            else:
                grade = "F"

            print("==== Student Result ====")
            print(f"Name        : {ALL_STUDENTS[i]['Name']}")
            print(f"Total marks : {total_marks}")
            print(f"Average     : {average:.2f}")
            print(f"Grade       : {grade}")

            return

    print("Student is not found")


def Class_Statistics():

    if len(ALL_STUDENTS) == 0:
        print("No students available")
        return

    total_students = len(ALL_STUDENTS)
    total_class_marks = 0
    highest_marks = 0
    lowest_marks = 0
    passed_students = 0
    failed_students = 0

    for i in range(len(ALL_STUDENTS)):

        total_marks = 0

        for j in range(len(ALL_STUDENTS[i]["Marks"])):
            total_marks += ALL_STUDENTS[i]["Marks"][j]

        total_class_marks += total_marks

        if i == 0:
            highest_marks = total_marks
            lowest_marks = total_marks
        else:
            if total_marks > highest_marks:
                highest_marks = total_marks

            if total_marks < lowest_marks:
                lowest_marks = total_marks

        average = total_marks / len(ALL_STUDENTS[i]["Marks"])

        if average >= 40:
            passed_students += 1
        else:
            failed_students += 1

    class_average = total_class_marks / total_students

    print("========== Class Statistics ==========")
    print(f"Total Students  : {total_students}")
    print(f"Class Average   : {class_average:.2f}")
    print(f"Highest Marks   : {highest_marks}")
    print(f"Lowest Marks    : {lowest_marks}")
    print(f"Passed Students : {passed_students}")
    print(f"Failed Students : {failed_students}")


while True:

    print("===============================================")
    print("           Student Grade Management")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Result")
    print("7. class Statistics")
    print("8. Exit")

    choose = int(input("Enter Your Choose : "))

    match choose:

        case 1:
            Add_student()

        case 2:
            Display_students()

        case 3:
            Search_student()

        case 4:
            Update_student()

        case 5:
            Delete_student()

        case 6:
            student_Result()

        case 7:
            Class_Statistics()

        case 8:
            print("Thank you")
            break

        case _:
            print("Enter Valid number ")