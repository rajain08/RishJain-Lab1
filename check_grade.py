from student_file import Student
from professor_file import Professor
from course_file import Course
from login_file import LoginUser
from grade_file import Grade
import time
import csv

INTERACTIVE = True

class check_my_grade_app():
    def __init__(self):
        self.student = Student()
        self.student.read_into_students()

        self.professor = Professor()
        self.professor.read_into_professors()

        self.course = Course()
        self.course.read_into_courses()

        self.login = LoginUser()
        self.login.read_into_logins()

        self.grade = Grade()
        self.grade.read_into_grades()
    
    def grade_stats(self):
        total_marks = 0
        count = 0
        course1 = input("What is the course you would like to get grade statistics on?: ")

        found = False

        current = self.grade.grades.head
        while current:
            if current.data["course_id"] == course1:
                curr = self.grade.grades.head
                grade_found = False

                temp_list = []
                while curr:
                    if curr.data["course_id"] == course1:
                        marks = int(curr.data.get("marks", 0))
                        total_marks += marks
                        count += 1
                        temp_list.append(marks)
                        grade_found = True
                    curr = curr.next
                
                if not grade_found:
                    print(f"No grades found for course {course1}")
                    return
                
                found = True
            
            current = current.next
        
        if not found:
            print("No course found")
            return
        
        temp_list.sort()
        n = len(temp_list)
        
        if n % 2 == 1:
            median_marks = temp_list[n // 2]
        else:
            median_marks = (temp_list[n // 2 - 1] + temp_list[n // 2]) / 2
        
        avg_marks = total_marks/count
        if avg_marks >= 90:
            avg_grade = "A"
        elif avg_marks >= 80:
            avg_grade = "B"
        elif avg_marks >= 70:
            avg_grade = "C"
        elif avg_marks >= 60:
            avg_grade = "D"
        else:
            avg_grade = "F"
        
        if median_marks >= 90:
            median_grade = "A"
        elif median_marks >= 80:
            median_grade = "B"
        elif median_marks >= 70:
            median_grade = "C"
        elif median_marks >= 60:
            median_grade = "D"
        else:
            median_grade = "F"
        
        print(f"The average marks of course {course1} was {avg_marks} to come out to an average grade of {avg_grade}")
        print(f"The median marks of course {course1} was {median_marks} to come out to an average grade of {median_grade}")

    def display_course_grade_report(self):
        course1 = input("What is the course you would like to get a grade report on?: ")

        grade_found = False
        curr = self.grade.grades.head

        while curr:
            if curr.data["course_id"] == course1:
                grade_found = True
                break
            curr = curr.next

        if not grade_found:
            print(f"\nNo grades found for course {course1}")
            return

        col_names = ["Email Address", "Course ID", "Grade", "Marks"]
        col_widths = [25, 15, 10, 10]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}}")
        print("========================================================================================")

        curr = self.grade.grades.head
        while curr:
            if curr.data["course_id"] == course1:
                email = str(curr.data.get("email_address", "N/A"))[:col_widths[0]]
                course_id = str(curr.data.get("course_id", "N/A"))[:col_widths[1]]
                grade = str(curr.data.get("grades", "N/A"))[:col_widths[2]]
                marks = str(curr.data.get("marks", "N/A"))[:col_widths[3]]

                print(f"{email:<{col_widths[0]}} {course_id:<{col_widths[1]}} {grade:<{col_widths[2]}} {marks:<{col_widths[3]}}")

            curr = curr.next

    def display_professor_grade_report(self):
        prof1 = input("What is the professor that you would like to get a grade report on?: ")

        current = self.professor.professors.head
        prof_found = False

        while current:
            if current.data["professor_id"] == prof1:
                prof_found = True
                course1 = current.data["course_id"]
                print(f"\nProfessor {prof1} is a {current.data["rank"]} of course {course1}")
                break
            current = current.next
        
        if not prof_found:
            print(f"\nNo grades found for professor {prof1}")
            return
        
        col_names = ["Email Address", "Course ID", "Grade", "Marks"]
        col_widths = [25, 15, 10, 10]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}}")
        print("========================================================================================")

        curr = self.grade.grades.head
        while curr:
            if curr.data["course_id"] == course1:
                email = str(curr.data.get("email_address", "N/A"))[:col_widths[0]]
                course_id = str(curr.data.get("course_id", "N/A"))[:col_widths[1]]
                grade = str(curr.data.get("grades", "N/A"))[:col_widths[2]]
                marks = str(curr.data.get("marks", "N/A"))[:col_widths[3]]

                print(f"{email:<{col_widths[0]}} {course_id:<{col_widths[1]}} {grade:<{col_widths[2]}} {marks:<{col_widths[3]}}")

            curr = curr.next
        
    def display_student_grade_report(self):
        student1 = input("What is the student you would like to get a grade report on?: ")

        student_found = False
        curr = self.grade.grades.head

        while curr:
            if curr.data["email_address"] == student1:
                student_found = True
                break
            curr = curr.next

        if not student_found:
            print(f"\nNo grades found for student: {student1}")
            return

        col_names = ["Email Address", "Course ID", "Grade", "Marks"]
        col_widths = [25, 15, 10, 10]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}}")
        print("========================================================================================")

        curr = self.grade.grades.head
        while curr:
            if curr.data["email_address"] == student1:
                email = str(curr.data.get("email_address", "N/A"))[:col_widths[0]]
                course_id = str(curr.data.get("course_id", "N/A"))[:col_widths[1]]
                grade = str(curr.data.get("grades", "N/A"))[:col_widths[2]]
                marks = str(curr.data.get("marks", "N/A"))[:col_widths[3]]

                print(f"{email:<{col_widths[0]}} {course_id:<{col_widths[1]}} {grade:<{col_widths[2]}} {marks:<{col_widths[3]}}")

            curr = curr.next
    
    def print_results(self, **kwargs):
        col_names = ["Email Address", "First Name", "Last Name", "Course ID", "Grade", "Marks"]
        col_widths = [25, 15, 15, 15, 8, 8]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}} {col_names[4]:<{col_widths[4]}} {col_names[5]:<{col_widths[5]}}")
        print("========================================================================================")

        curr = self.student.students.head
        while curr:
            if all(curr.data[key] == value for key, value in kwargs.items()):
                email_address = str(curr.data.get('email_address', 'N/A'))[:col_widths[0]]
                first_name = str(curr.data.get('first_name', 'N/A'))[:col_widths[1]]
                last_name = str(curr.data.get('last_name', 'N/A'))[:col_widths[2]]
                course_id = str(curr.data.get('course_id', 'N/A'))[:col_widths[3]]
                grades = str(curr.data.get('grades', 'N/A'))[:col_widths[4]]
                marks = str(curr.data.get('marks', 'N/A'))[:col_widths[5]]

                print(f"{email_address:<{col_widths[0]}} {first_name:<{col_widths[1]}} {last_name:<{col_widths[2]}} {course_id:<{col_widths[3]}} {grades:<{col_widths[4]}} {marks:<{col_widths[5]}}")

            curr = curr.next

    def search(self):
        entered = input("Do you want to search by student email (email), first name (first), last name (last), course, or grade?: ")
        
        if entered == "email":
            email = input("What is the student email you would like to find?: ")

            start = time.time()

            found = False
            curr = self.student.students.head

            while curr:
                if curr.data["email_address"] == email:
                    found = True
                    break
                curr = curr.next
            
            end = time.time()

            if not found:
                print(f"\nNo records found for student: {email}")
                return
            else:
                self.print_results(email_address=email)
                elapsed = end - start
                print(f"\nSearch completed in {elapsed:.15f} seconds.")
        
        elif entered == "first":
            first = input("What is the student first name you would like to find?: ")

            start = time.time()

            found = False
            curr = self.student.students.head

            while curr:
                if curr.data["first_name"] == first:
                    found = True
                    break
                curr = curr.next
            
            end = time.time()

            if not found:
                print(f"\nNo records found for student first name: {first}")
                return
            else:
                self.print_results(first_name=first)
                elapsed = end - start
                print(f"\nSearch completed in {elapsed:.15f} seconds.")

        elif entered == "last":
            last = input("What is the student last name you would like to find?: ")

            start = time.time()

            found = False
            curr = self.student.students.head

            while curr:
                if curr.data["last_name"] == last:
                    found = True
                    break
                curr = curr.next
            
            end = time.time()

            if not found:
                print(f"\nNo records found for student last name: {last}")
                return
            else:
                self.print_results(last_name=last)
                elapsed = end - start
                print(f"\nSearch completed in {elapsed:.15f} seconds.")

        elif entered == "course":
            course = input("What is the course id you would like to find?: ")

            start = time.time()

            found = False
            curr = self.student.students.head

            while curr:
                if curr.data["course_id"] == course:
                    found = True
                    break
                curr = curr.next
            
            end = time.time()

            if not found:
                print(f"\nNo records found for course id: {course}")
                return
            else:
                self.print_results(course_id=course)
                elapsed = end - start
                print(f"\nSearch completed in {elapsed:.15f} seconds.")

        elif entered == "grade":
            grade = input("What is the student grade you would like to find?: ")

            start = time.time()

            found = False
            curr = self.student.students.head

            while curr:
                if curr.data["grades"] == grade:
                    found = True
                    break
                curr = curr.next
            
            end = time.time()

            if not found:
                print(f"\nNo records found for grade: {grade}")
                return
            else:
                self.print_results(grades=grade)
                elapsed = end - start
                print(f"\nSearch completed in {elapsed:.15f} seconds.")

        else:
            print("Invalid input.")
    
    def update_sorted_csv(self, sorted_data):
        with open('student.csv', mode='w', newline='') as file:
            fieldnames = sorted_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_data)

    def sorting(self):
        ll = self.student.students

        entered = input("Do you want to sort by student email or marks?: ")

        if entered == "email":
            choice = input("Do you want to sort in desc order (True or False): ")
            if choice not in["True", "False", "true", "false"]:
                print("Invalid choice")
                return
            
            choice = choice.strip().lower() == 'true'

            with open('student.csv', mode='r') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            start = time.time()

            sorted_data = sorted(data, key=lambda x: x['email_address'], reverse = choice)

            end = time.time()

            elapsed = end - start
            print(f"\nSorting completed in {elapsed:.15f} seconds")

            ll.head = None

            for row in sorted_data:
                ll.add_last(**row)
            
            self.update_sorted_csv(sorted_data)
            print("Sorted by email successfully")

        elif entered == "marks":
            choice = input("Do you want to sort in desc order (True or False): ")
            if choice not in["True", "False", "true", "false"]:
                print("Invalid input.")
                return
            
            choice = choice.strip().lower() == 'true'

            with open('student.csv', mode='r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            
            start = time.time()
            
            sorted_data = sorted(data, key=lambda x: int(x['marks']) if x['marks'].isdigit() else 0, reverse = choice)

            end = time.time()

            ll.head = None

            elapsed = end - start
            print(f"\nSorting completed in {elapsed:.15f} seconds.")

            for row in sorted_data:
                ll.add_last(**row)
            
            self.update_sorted_csv(sorted_data)
            print("Sorted by marks successfully")

        else:
            print("Invalid input.")
