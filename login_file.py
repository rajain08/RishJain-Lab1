from linked_list import LinkedList
import csv
import getpass

class TextSecurity:
    def __init__(self, shift):
        self.shifter = shift
        self.s = self.shifter % 26

    def _convert(self, text, s):
        result = ""
        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) + s - 65) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) + s - 97) % 26 + 97)
            else:
                result += ch
        return result

    def encrypt(self, text):
        return self._convert(text, self.shifter)

    def decrypt(self, text):
        return self._convert(text, 26 - self.s)

class LoginLinkedList(LinkedList):
    def __init__(self, email_id: str, password: str, role: str):
        super().__init__()
        self.email_id = email_id
        self.password = password
        self.role = role

class LoginUser():
    def __init__(self):
        self.logins = LoginLinkedList(email_id=None, password=None, role=None)
    
    def read_into_logins(self):
        with open('login.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.logins.add_last(**row)
    
    def update_login_csv(self):
        with open("login.csv", mode="w", newline='') as file:
            fieldnames = ["user_id", "password", "role"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            current = self.logins.head
            while current:
                writer.writerow({
                    "user_id": current.data["user_id"],
                    "password": current.data["password"],
                    "role": current.data["role"]
                })
                current = current.next
    
    def login(self):
        try:
            user_id = input("Enter email_address: ")
            en_password = getpass.getpass("Enter password: ")
            password = self.encrypt_password(en_password)

            current = self.logins.head
            while current:
                if "user_id" in current.data and "password" in current.data:
                    if current.data["user_id"] == user_id:
                        if current.data["password"] == password:  
                            print(f"Login successful! Welcome {current.data.get('role', None)}!")
                            return current.data.get("role", None), current.data.get("user_id", None), current.data.get("password", None)
                        else:
                            print("Incorrect password. Please try again.")
                            return None, None, None

                current = current.next
            
            print("Username not found. Please try again.")
            return None, None, None

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
            return None, None, None

    def signup(self):
        print("\nSignup screen:")
        while True:
            user_id = input("Enter email address/user id: ")
            
            current = self.logins.head
            flag = False
            
            while current:
                if current.data["user_id"] == user_id:
                    flag = True
                    break
                current = current.next

            if flag:
                print("\nEmail/user id already exists. Please choose another.")
            else:
                break

        password = getpass.getpass("Enter password: ")
        coded = self.encrypt_password(password)

        role = input("Enter role: ")
        while role not in ["student", "professor"]:
            role = input("Invalid choice. Enter role student or professor: ")
        
        self.logins.add_last(user_id=user_id, password=coded, role=role)

        self.update_login_csv()
        
        print("Signup successful! You can now log in.")

    def change_password(self, user_id):
        new_pass = input("Please enter the new password: ")
        
        current = self.logins.head
        while current:
            if "user_id" in current.data:
                if current.data["user_id"] == user_id:
                    coded = self.encrypt_password(new_pass)
                    current.data["password"] = coded
                    print("Password changed successfully.")
                    break

            current = current.next
        
        self.update_login_csv()
    
    def encrypt_password(self, password):
        cipher = TextSecurity(4)
        coded = cipher.encrypt(password)
        return coded

    def decrypt_password(self, password):
        cipher = TextSecurity(4)
        decoded = cipher.decrypt(password)
        return decoded
