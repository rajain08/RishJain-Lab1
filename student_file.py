from linked_list import LinkedList
import csv

class StudentLinkedList(LinkedList):
    def __init__(self, email_address: str, first_name: str, last_name: str, course_id: str, grades: str, marks: int):
        super().__init__()
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grades = grades
        self.marks = marks

class Student():
    def __init__(self):
        self.students = StudentLinkedList(email_address=None,first_name=None, last_name=None, course_id=None, grades=None, marks=0)
    
    def read_into_students(self):
        with open('student.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.students.add_last(**row)
    
    def update_student_csv(self):
        with open("student.csv", mode="w", newline='') as file:
            fieldnames = ["email_address", "first_name", "last_name", "course_id", "grades", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            current = self.students.head
            while current:
                writer.writerow({
                    "email_address": current.data["email_address"],
                    "first_name": current.data["first_name"],
                    "last_name": current.data["last_name"],
                    "course_id": current.data["course_id"],
                    "grades": current.data["grades"],
                    "marks": current.data["marks"]
                })
                current = current.next

    def display_records(self):
        col_names = ["Email Address", "First Name", "Last Name", "Course ID", "Grades", "Marks"]
        col_widths = [25, 15, 15, 15, 8, 8]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}} {col_names[4]:<{col_widths[4]}} {col_names[5]:<{col_widths[5]}}")
        print("========================================================================================")
        current = self.students.head
        while current:
            email_address = str(current.data.get('email_address', 'N/A'))[:col_widths[0]]
            first_name = str(current.data.get('first_name', 'N/A'))[:col_widths[1]]
            last_name = str(current.data.get('last_name', 'N/A'))[:col_widths[2]]
            course_id = str(current.data.get('course_id', 'N/A'))[:col_widths[3]]
            grades = str(current.data.get('grades', 'N/A'))[:col_widths[4]]
            marks = str(current.data.get('marks', 'N/A'))[:col_widths[5]]

            print(f"{email_address:<{col_widths[0]}} {first_name:<{col_widths[1]}} {last_name:<{col_widths[2]}} {course_id:<{col_widths[3]}} {grades:<{col_widths[4]}} {marks:<{col_widths[5]}}")
            current = current.next
    
    def display_record_by_student(self, user_id):
        col_names = ["Email Address", "First Name", "Last Name", "Course ID", "Grades", "Marks"]
        col_widths = [25, 15, 15, 15, 8, 8]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}} {col_names[4]:<{col_widths[4]}} {col_names[5]:<{col_widths[5]}}")
        print("========================================================================================")
        current = self.students.head
        flag = False

        while current:
            email_address = str(current.data.get('email_address', 'N/A'))[:col_widths[0]]
            first_name = str(current.data.get('first_name', 'N/A'))[:col_widths[1]]
            last_name = str(current.data.get('last_name', 'N/A'))[:col_widths[2]]
            course_id = str(current.data.get('course_id', 'N/A'))[:col_widths[3]]
            grades = str(current.data.get('grades', 'N/A'))[:col_widths[4]]
            marks = str(current.data.get('marks', 'N/A'))[:col_widths[5]]

            if current.data["email_address"] == user_id:
                print(f"{email_address:<{col_widths[0]}} {first_name:<{col_widths[1]}} {last_name:<{col_widths[2]}} {course_id:<{col_widths[3]}} {grades:<{col_widths[4]}} {marks:<{col_widths[5]}}")
                flag = True
            
            current = current.next

            if not flag:
                print("No records found.")

    def add_new_student(self):
        new_email_address = input("Please enter the new email address: ")
        current = self.students.head

        while current:
            if current.data["email_address"] == new_email_address:
                print("Student already exists")
                return
            current = current.next

        first_name = input("Please enter the new first name: ")
        last_name = input("Please enter the new last name: ")
        course_id = input("Please enter new course id: ")
        while True:
            try:
                marks = int(input("Please enter the new marks (0-100): "))
                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100")
            except ValueError:
                print("Invalid input")
            
        if marks >= 90:
            grades = "A"
        elif marks >= 80:
            grades = "B"
        elif marks >= 70:
            grades = "C"
        elif marks >= 60:
            grades = "D"
        else:
            grades = "F"
        
        self.students.add_last(email_address=new_email_address, first_name=first_name, last_name=last_name, course_id=course_id, grades=grades, marks=marks)

        self.update_student_csv()

    def delete_student(self):
        deleted_student = input("What is the email address of the student that you would like to delete?: ")
        
        if self.students.delete_node(email_address=deleted_student):
            print("Student deleted successfully")
        
        self.update_student_csv()

    def check_my_grades(self, user_id):
        col_names = ["Course ID", "Grades"]
        col_widths = [15, 8]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}}")
        print("========================================================================================")
        current = self.students.head
        flag = False

        while current:
            course_id = str(current.data.get('course_id', 'N/A'))[:col_widths[0]]
            grades = str(current.data.get('grades', 'N/A'))[:col_widths[1]]

            if current.data["email_address"] == user_id:
                print(f"{course_id:<{col_widths[0]}} {grades:<{col_widths[1]}}")
                flag = True
            
            current = current.next

            if not flag:
                print("No records found.")
    
    def check_my_marks(self, user_id):
        col_names = ["Course ID", "Marks"]
        col_widths = [15, 8]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}}")
        print("========================================================================================")
        current = self.students.head
        flag = False

        while current:
            course_id = str(current.data.get('course_id', 'N/A'))[:col_widths[0]]
            grades = str(current.data.get('marks', 'N/A'))[:col_widths[1]]

            if current.data["email_address"] == user_id:
                print(f"{course_id:<{col_widths[0]}} {grades:<{col_widths[1]}}")
                flag = True
            
            current = current.next

            if not flag:
                print("No records found.")

    def update_student_record(self):
        user_id = input("Please enter the email address of the student that you want to update: ")
        flag = False

        current = self.students.head
        while current:
            if "email_address" in current.data and current.data["email_address"] == user_id:
                    current.data["email_address"] = input("Please enter the updated email address: ")
                    current.data["first_name"] = input("Please enter the updated first name: ")
                    current.data["last_name"] = input("Please enter the updated last name: ")
                    current.data["course_id"] = input("Please enter the updated course id: ")
                    while True:
                        try:
                            current.data["marks"] = int(input("Please enter the new marks (0-100): "))
                            if 0 <= current.data["marks"] <= 100:
                                break
                            else:
                                print("Marks must be between 0 and 100")
                        except ValueError:
                            print("Invalid input")
                    
                    if current.data["marks"] >= 90:
                        current.data["grades"] = "A"
                    elif current.data["marks"] >= 80:
                        current.data["grades"] = "B"
                    elif current.data["marks"] >= 70:
                        current.data["grades"] = "C"
                    elif current.data["marks"] >= 60:
                        current.data["grades"] = "D"
                    else:
                        current.data["grades"] = "F"
                    flag = True
                    break
            current = current.next
            
        if not flag:
            print("No records found.")
        
        self.update_student_csv()
