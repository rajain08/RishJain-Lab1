from linked_list import LinkedList
from course_file import Course
import csv

class ProfessorLinkedList(LinkedList):
    def __init__(self, name: str, email_address: str, rank: str, course_id: str):
        super().__init__()
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

class Professor():
    def __init__(self):
        self.professors = ProfessorLinkedList(name=None, email_address=None, rank=None, course_id=None)
    
    def read_into_professors(self):
        with open('professor.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.professors.add_last(**row)
    
    def update_professor_csv(self):
        with open("professor.csv", mode="w", newline='') as file:
            fieldnames = ["professor_id", "professor_name", "rank", "course_id"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            current = self.professors.head
            while current:
                writer.writerow({
                    "professor_id": current.data["professor_id"],
                    "professor_name": current.data["professor_name"],
                    "rank": current.data["rank"],
                    "course_id": current.data["course_id"]
                })
                current = current.next
    
    def professors_details(self):
        col_names = ["Professor ID", "Name", "Rank", "Course ID"]
        col_widths = [25, 25, 25, 10]

        print("\n=======================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}} {col_names[3]:<{col_widths[3]}}")
        print("=======================================================================================")
        current = self.professors.head
        while current:
            professor_id = str(current.data.get('professor_id', 'N/A'))[:col_widths[0]]
            professor_name = str(current.data.get('professor_name', 'N/A'))[:col_widths[1]]
            rank = str(current.data.get('rank', 'N/A'))[:col_widths[2]]
            course_id = str(current.data.get('course_id', 'N/A'))[:col_widths[3]]

            print(f"{professor_id:<{col_widths[0]}} {professor_name:<{col_widths[1]}} {rank:<{col_widths[2]}} {course_id:<{col_widths[3]}}")
            current = current.next

    def add_new_professor(self):
        new_prof_id = input("Please enter the new professor id: ")
        current = self.professors.head
            
        while current:
            if current.data["professor_id"] == new_prof_id:
                print("Professor already exists")
                return
            current = current.next
            
        new_prof_name = input("Please enter the new professor name: ")
        new_rank = input("Please enter the new professor rank: ")
        new_course_id = input("Please enter the new course id: ")
        
        self.professors.add_last(professor_id=new_prof_id, professor_name=new_prof_name, rank=new_rank, course_id=new_course_id)

        self.update_professor_csv()

    def delete_professor(self):
        deleted_professor = input("What is the email address of the professor that you would like to delete?: ")
        
        if self.professors.delete_node(professor_id=deleted_professor):
            print("Professor deleted successfully")
        
        self.update_professor_csv()

    def modify_professor_details(self):
        new_prof_id = input("Please enter the id of the professor that you want to update: ")
        flag = False

        current = self.professors.head
        while current:
            if "professor_id" in current.data and current.data["professor_id"] == new_prof_id:
                    current.data["professor_id"] = input("Please enter the updated professor id: ")
                    current.data["professor_name"] = input("Please enter the updated professor name: ")
                    current.data["rank"] = input("Please enter the updated rank: ")
                    current.data["course_id"] = input("Please enter the updated course_id: ")
                    flag = True
                    break
                
            current = current.next
            
        if not flag:
            print("No records found.")
        
        self.update_professor_csv()

    def show_course_details_by_professor(self):
        self.c1 = Course()
        self.c1.read_into_courses()

        self.p1 = Professor()
        self.p1.read_into_professors()

        prof1 = input("What is the professor that you would like to get course details on?: ")

        current = self.p1.professors.head
        prof_found = False

        while current:
            if current.data["professor_id"] == prof1:
                prof_found = True
                course1 = current.data["course_id"]
                print(f"\nProfessor {prof1} is a {current.data["rank"]} of course {course1}")
                break
            current = current.next
        
        if not prof_found:
            print(f"\nNo course found for professor {prof1}")
            return
        
        col_names = ["Course ID", "Course Name", "Description"]
        col_widths = [10, 25, 100]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}}")
        print("========================================================================================")

        curr = self.c1.courses.head
        while curr:
            if curr.data["course_id"] == course1:
                course_id = str(curr.data.get("course_id", "N/A"))[:col_widths[0]]
                course_name = str(curr.data.get("course_name", "N/A"))[:col_widths[1]]
                description = str(curr.data.get("description", "N/A"))[:col_widths[2]]

                print(f"{course_id:<{col_widths[0]}} {course_name:<{col_widths[1]}} {description:<{col_widths[2]}}")

            curr = curr.next