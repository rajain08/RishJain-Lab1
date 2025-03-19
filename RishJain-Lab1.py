from check_grade import check_my_grade_app

def check_my_grade_menu():
    student = check_my_grade_app().student
    professor = check_my_grade_app().professor
    course = check_my_grade_app().course
    login = check_my_grade_app().login
    grade = check_my_grade_app().grade
    check_my_grade = check_my_grade_app()

    while True:
        print("\nWelcome to the Check My Grade Main Menu!:")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            role, user_id, password = login.login()

            if role is None:
                print("Login failed.")

            elif role == "professor":
                while True:
                    print("\nWhat section do you want to choose?")
                    print("1. Students")
                    print("2. Courses")
                    print("3. Professors")
                    print("4. Grades")
                    print("5. Password")
                    print("6. CHECK MY GRADE APP")
                    print("7. Exit")
                    answer = input("Enter your choice: ")

                    if answer == "1":
                        while True:
                            print("\nWhat would you like to do?")
                            print("1. Display records")
                            print("2. Add new student")
                            print("3. Delete student")
                            print("4. Update student record")
                            print("5. Exit")
                            ans = input("Enter your choice: ")
                            if ans == "1":
                                student.display_records()
                            elif ans == "2":
                                student.add_new_student()
                            elif ans == "3":
                                student.delete_student()
                            elif ans == "4":
                                student.update_student_record()
                            elif ans == "5":
                                break
                            else:
                                print("Invalid choice. Please try again.")

                    elif answer == "2":
                        while True:
                            print("\nWhat would you like to do?")
                            print("1. Display courses")
                            print("2. Add new course")
                            print("3. Delete course")
                            print("4. Modify course")
                            print("5. Exit")
                            ans = input("Enter your choice: ")
                            if ans == "1":
                                course.display_courses()
                            elif ans == "2":
                                course.add_new_course()
                            elif ans == "3":
                                course.delete_course()
                            elif ans == "4":
                                course.modify_course()
                            elif ans == "5":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    
                    elif answer == "3":
                        while True:
                            print("\nWhat would you like to do?")
                            print("1. Display professor details")
                            print("2. Add new professor")
                            print("3. Delete professor")
                            print("4. Modify professor details")
                            print("5. Show course details by professor")
                            print("6. Exit")
                            ans = input("Enter your choice: ")
                            if ans == "1":
                                professor.professors_details()
                            elif ans == "2":
                                professor.add_new_professor()
                            elif ans == "3":
                                professor.delete_professor()
                            elif ans == "4":
                                professor.modify_professor_details()
                            elif ans == "5":
                                professor.show_course_details_by_professor()
                            elif ans == "6":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    
                    elif answer == "4":
                        while True:
                            print("\nWhat would you like to do?")
                            print("1. Add/modify grade")
                            print("2. Delete grade")
                            print("3. Exit")
                            ans = input("Enter your choice: ")
                            if ans == "1":
                                grade.add_grade()
                            elif ans == "2":
                                grade.delete_grade()
                            elif ans == "3":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    
                    elif answer == "5":
                        while True:
                            print("\nWhat would you like to do?")
                            print("1. Decrypt password")
                            print("2. Change password")
                            print("3. Exit")
                            ans = input("Enter your choice: ")
                            if ans == "1":
                                print(f"Your encrypted password in the database is {password}")
                                decoded = login.decrypt_password(password)
                                print(f"Your decrypted password is {decoded}")                                
                            elif ans == "2":
                                login.change_password(user_id)
                                login.read_into_logins()

                                current = login.logins.head
                                while current:
                                    if current.data["user_id"] == user_id:
                                        password = current.data["password"]
                                        break
                                    current = current.next
                            elif ans == "3":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    
                    elif answer == "6":
                        while True:
                            print("\nWhat would you like to do?")
                            print("1. Search records")
                            print("2. Sort records")
                            print("3. Get grade statistics of course")
                            print("4. Display student grade report")
                            print("5. Display course grade report")
                            print("6. Display professor grade report")
                            print("7. Exit")
                            ans = input("Enter your choice: ")
                            if ans == "1":
                                check_my_grade.search()
                            elif ans == "2":
                                check_my_grade.sorting()
                            elif ans == "3":
                                check_my_grade.grade_stats()
                            elif ans == "4":
                                check_my_grade.display_student_grade_report()
                            elif ans == "5":
                                check_my_grade.display_course_grade_report()
                            elif ans == "6":
                                check_my_grade.display_professor_grade_report()
                            elif ans == "7":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    
                    elif answer == "7":
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif role == "student":
                while True:
                    print("\nWhat would you like to do?")
                    print("1. Display records")
                    print("2. Check my grades")
                    print("3. Check my marks")
                    print("4. Display courses")
                    print("5. Change password")
                    print("6. Exit")
                    answer = input("Enter your choice: ")
                    if answer == "1":
                        student.display_record_by_student(user_id)
                    elif answer == "2":
                        student.check_my_grades(user_id)
                    elif answer == "3":
                        student.check_my_marks(user_id)
                    elif answer == "4":
                        course.display_courses()
                    elif answer == "5":
                        login.change_password(user_id)
                    elif answer == "6":
                        break

        elif choice == "2":
            login.signup()
        
        elif choice == "3":
            print("Thank you. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    check_my_grade_menu()
