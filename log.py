# Student Login Module

# Sample student database with roll numbers and passwords
students = {
    "101": "ravi123",
    "102": "anita123",
    "103": "rahul456"
}

def student_login():
    print("--- Student Login ---")
    roll = input("Enter Roll Number: ")
    password = input("Enter Password: ")

    if roll in students:
        if students[roll] == password:
            print(f"Login successful! Welcome student {roll}.")
        else:
            print("Incorrect password. Try again.")
    else:
        print("Roll number not found. Please check again.")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_login()
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
