from linked_list import LinkedList
import csv

class GradeLinkedList(LinkedList):
    def __init__(self, email_address: str, course_id : str, grade: str, marks: int):
        super().__init__()
        self.email_address = email_address
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

class Grade():
    def __init__(self):
        self.grades = GradeLinkedList(email_address=None, course_id=None, grade=None, marks=0)
    
    def read_into_grades(self):
        with open('student.csv', mode='r', newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                grade_data = {
                    "email_address": row.get("email_address", "N/A"),  
                    "course_id": row.get("course_id", "N/A"),
                    "grades": row.get("grades", "N/A"),
                    "marks": row.get("marks", "N/A")
                }

                self.grades.add_last(**grade_data)
    
    def update_grade_csv(self, email, course_id, new_grade, new_marks):
        students_data = []
        with open('student.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["email_address"] == email and row["course_id"] == course_id:
                    row["grades"] = new_grade
                    row["marks"] = new_marks
                students_data.append(row)
        
        with open('student.csv', mode='w', newline='') as file:
            fieldnames = ["email_address", "first_name", "last_name", "course_id", "grades", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students_data:
                writer.writerow(student)

    def add_grade(self):
        email = input("What student would you like to add a grade for?: ")

        current = self.grades.head
        student_found = False

        while current:            
            course_id = current.data["course_id"]
            if current.data["email_address"] == email:
                student_found = True

                if current.data["grades"] != "N/A":
                    grade_edit = input("A grade already exists. Would you like to edit the grade? (y/n): ")
                    while grade_edit not in ["y", "n"]:
                        grade_edit = input("Invalid input. Would you like to edit the grade? (y/n): ")
                    if grade_edit == "n":
                        return
                
                while True:
                    try:
                        new_marks = int(input("\nPlease enter the new marks (integer value): "))
                        if 0 <= new_marks <= 100:
                            break
                        else:
                            print("Marks must be between 0 and 100. Please try again")
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer")

                current.data["marks"] = new_marks

                if new_marks >= 90:
                    new_grade = "A"
                elif new_marks >= 80:
                    new_grade = "B"
                elif new_marks >= 70:
                    new_grade = "C"
                elif new_marks >= 60:
                    new_grade = "D"
                else:
                    new_grade = "F"
                
                current.data["grades"] = new_grade
                print("Grade and marks modified successfully")
                break
            
            current = current.next

        if not student_found:
            print("Student not found")
            return
        
        self.update_grade_csv(email, course_id, new_grade, new_marks)

    def delete_grade(self):
        del_email = input("What is the email address of the grade that you would like to delete?: ")
        
        updated = False

        current = self.grades.head
        while current:
            del_course = current.data["course_id"]
            if current.data["email_address"] == del_email:
                new_grade = current.data["grades"] = "N/A"
                new_marks = current.data["marks"] = 0
                updated = True
                break
            current = current.next

        if updated:
            print("Grade and marks deleted successfully")
            self.update_grade_csv(del_email, del_course, new_grade, new_marks)
        else:
            print("No record found.")
