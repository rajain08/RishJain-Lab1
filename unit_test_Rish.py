import unittest, time, csv, random, names
from unittest.mock import patch
from check_grade import check_my_grade_app

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        """Set up the test environment and initialize the app."""
        self.app = check_my_grade_app()

    def generate_students(self, num_records):
        """Generate and write student records to student.csv."""
        # Reset students data for a clean start
        self.app.student.students.head = None

        start = time.time()

        with open("student.csv", mode='w', newline='') as file:
            fieldnames = ["email_address", "first_name", "last_name", "course_id", "grades", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(num_records):
                marks = random.randint(0, 100)
                grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "F"
                first_name = names.get_first_name()
                last_name = names.get_last_name()

                writer.writerow({
                    "email_address": f"{first_name.lower()}.{last_name.lower()}{i}@university.edu",
                    "first_name": first_name,
                    "last_name": last_name,
                    "course_id": f"CS{i%10 + 101}",
                    "grades": grade,
                    "marks": str(marks)
                })
        
        end = time.time()
        elapsed = end - start
        print(f"{num_records} student records generated in {elapsed:.15f} seconds")

    @patch("builtins.input", side_effect=["new_student@csu.edu", "John", "Doe", "CS101", 89])
    def test_add_student(self, mock_input):
        start = time.time()
        self.app.student.add_new_student()
        end = time.time()
        elapsed = end - start
        print(f"Add student completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Add took too long")

    @patch("builtins.input", side_effect=["new_student@csu.edu", "nstudent@csu.edu", "new_first_name", "new_last_name", "new_course", 75])
    def test_modify_student(self, mock_input):
        start = time.time()
        self.app.student.update_student_record()
        end = time.time()
        
        elapsed = end - start
        print(f"Modify student completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Modify took too long")
    
    @patch("builtins.input", side_effect=["nstudent@csu.edu"])
    def test_delete_student(self, mock_input):
        start = time.time()
        self.app.student.delete_student()
        end = time.time()
        elapsed = end - start
        print(f"Delete student completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Delete took too long")


class TestCourseManagement(unittest.TestCase):

    def setUp(self):
        """Set up the test environment by initializing check_my_grade_app and populating data."""
        self.app = check_my_grade_app()

    @patch("builtins.input", side_effect=["DATA111", "Intro to Python", "Gives an intro to Python"])  
    def test_add_course(self, mock_input):
        start = time.time()
        self.app.course.add_new_course()
        end = time.time()
        elapsed = end - start
        print(f"Add course completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Add took too long")
    
    @patch("builtins.input", side_effect=["DATA111", "DATA102","Intro to SQL", "Gives an intro to SQL"])
    def test_modify_course(self, mock_input):
        start = time.time()
        self.app.course.modify_course()
        end = time.time()
        elapsed = end - start
        print(f"Modify course completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Modify took too long")

    @patch("builtins.input", side_effect=["DATA102"])
    def test_delete_course(self, mock_input):
        start = time.time()
        self.app.course.delete_course()
        end = time.time()
        elapsed = end - start
        print(f"Delete course completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Delete took too long")

class TestProfessorManagement(unittest.TestCase):

    def setUp(self):
        self.app = check_my_grade_app()

    @patch("builtins.input", side_effect=["test_prof@mycsu.edu", "Professor Test", "Test Professor", "DATA101"])  
    def test_add_professor(self, mock_input):
        start = time.time()
        self.app.professor.add_new_professor()
        end = time.time()
        elapsed = end - start
        print(f"Add professor completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Add took too long")
    
    @patch("builtins.input", side_effect=["test_prof@mycsu.edu", "testprof@mycsu.edu","Professor Testing", "Testing Professor", "DATA201"])
    def test_modify_professor(self, mock_input):
        start = time.time()
        self.app.professor.modify_professor_details()
        end = time.time()
        elapsed = end - start
        print(f"Modify professor completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Modify took too long")

    @patch("builtins.input", side_effect=["testprof@mycsu.edu"])
    def test_delete_professor(self, mock_input):
        start = time.time()
        self.app.professor.delete_professor()
        end = time.time()
        elapsed = end - start
        print(f"Delete professor completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Delete took too long")

class TestSS(unittest.TestCase):

    def setUp(self):
        self.app = check_my_grade_app()

    # Search Tests
    @patch("builtins.input", side_effect=["email", "new_student@csu.edu"])
    def test_search_email(self, mock_input):
        start = time.time()
        self.app.search()
        end = time.time()
        elapsed = end - start
        print(f"Search by email completed in {elapsed:.15f} seconds.")
        self.assertTrue(elapsed < 1, "Search took too long.")

    @patch("builtins.input", side_effect=["grade", "A"])
    def test_search_grade(self, mock_input):
        start = time.time()
        self.app.search()
        end = time.time()
        elapsed = end - start
        print(f"Search by grade completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 1, "Search took too long")

    @patch("builtins.input", side_effect=["email", "false"])
    def test_sort_email(self, mock_input):
        start = time.time()
        self.app.sorting()
        end = time.time()
        elapsed = end - start
        print(f"Sort by email completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 2, "Sort took too long")

    @patch("builtins.input", side_effect=["marks", "True"])
    def test_sort_marks(self, mock_input):
        start = time.time()
        self.app.sorting()
        end = time.time()
        elapsed = end - start
        print(f"Sort by marks completed in {elapsed:.15f} seconds")
        self.assertTrue(elapsed < 2, "Sort took too long")

if __name__ == "__main__":
    ts = TestStudentManagement()
    ts.setUp()
    ts.generate_students(1000)
    #unittest.main(defaultTest="TestCourseManagement.test_add_course")
