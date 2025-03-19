from linked_list import LinkedList
import csv

class CourseLinkedList(LinkedList):
    def __init__(self, course_id: str, course_name: str, description: str):
        super().__init__()
        self.course_id = course_id
        self.course_name = course_name        
        self.description = description

class Course():
    def __init__(self):
        self.courses = CourseLinkedList(course_id=None, course_name=None, description=None)
    
    def read_into_courses(self):
        with open('course.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.courses.add_last(**row)
    
    def update_course_csv(self):
        with open("course.csv", mode="w", newline='') as file:
            fieldnames = ["course_id", "course_name", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            current = self.courses.head
            while current:
                writer.writerow({
                    "course_id": current.data["course_id"],
                    "course_name": current.data["course_name"],
                    "description": current.data["description"]
                })
                current = current.next
    
    def display_courses(self):
        col_names = ["Course ID", "Course Name", "Description"]
        col_widths = [10, 25, 100]

        print("\n========================================================================================")
        print(f"{col_names[0]:<{col_widths[0]}} {col_names[1]:<{col_widths[1]}} {col_names[2]:<{col_widths[2]}}")
        print("========================================================================================")
        current = self.courses.head
        while current:
            course_id = str(current.data.get('course_id', 'N/A'))[:col_widths[0]]
            course_name = str(current.data.get('course_name', 'N/A'))[:col_widths[1]]
            description = str(current.data.get('description', 'N/A'))[:col_widths[2]]

            print(f"{course_id:<{col_widths[0]}} {course_name:<{col_widths[1]}} {description:<{col_widths[2]}}")
            current = current.next

    def add_new_course(self):
        new_course_id = input("Please enter the new course id: ")
        current = self.courses.head
            
        while current:
            if current.data["course_id"] == new_course_id:
                print("Course already exists")
                return
            current = current.next
            
        new_course_name = input("Please enter the new course name: ")
        new_desc = input("Please enter the new description: ")
        
        self.courses.add_last(course_id=new_course_id, course_name=new_course_name, description=new_desc)

        print("\nCourse added successfully.")

        self.update_course_csv()

    def delete_course(self):
        deleted_course = input("What is the course id of the course that you would like to delete?: ")
        
        if self.courses.delete_node(course_id=deleted_course):
            print("Course deleted successfully")
        
        self.update_course_csv()

    def modify_course(self):
        course_id = input("Please enter the id of the course that you want to update: ")
        flag = False

        current = self.courses.head
        while current:
            if "course_id" in current.data and current.data["course_id"] == course_id:
                    current.data["course_id"] = input("Please enter the updated course id: ")
                    current.data["course_name"] = input("Please enter the updated course name: ")
                    current.data["description"] = input("Please enter the updated description: ")
                    flag = True
                    break
            
            current = current.next
            
        if not flag:
            print("No records found.")
        
        self.update_course_csv()
