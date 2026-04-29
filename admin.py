import os
from mamager import *
from chef import *
from customer import *

customer = "customer@example.com"

def login():
    attempts = 0  
    while attempts < 3:
        username = input("Enter the name: ")
        password = input("Enter password: ")

        username = username.lower()
        password = password.lower()

        if username == "admin" and password == "admin123":
            print("\nLogin successful!\n")
            admin_menu()
            return  
        elif username == "manager" and password == "manager123":
            print("\nLogin Successful!\n")
            manager_menu()
            return
        elif username == "chef" and password == "chef123":
            print("\nLogin Successful!\n")
            main_menu()
            return
        elif username == "customer" and password == "customer123":
            print("\nLogin Successful!\n")
            customer_menu(customer)
            return
        else:
            attempts += 1
            if attempts < 3:
                print("Incorrect username or password. Please try again.\n")
            else:
                print("Maximum login attempts reached. Exiting...\n")
    
# Call the login function
#login()



#ADMIN

def admin_menu():
    while True:
        print("\nPlease select an option from 1-4:")
        print("1. Manage staff")
        print("2. View sales")
        print("3. View feedback")
        print("4. Update own profile")
        print("5. Logout")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                manage_staff()
            elif choice == 2:
                view_sales()
            elif choice == 3:
                view_feedback()
            elif choice == 4:
                update_own_profile()
            elif choice == 5:
                print("Logging out...\n")
                break  
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")

def manage_staff():
    while True:
        print("\nManage Staff:")
        print("1. Add Staff")
        print("2. Edit Staff")
        print("3. Delete Staff")
        print("4. Go Back")

        try:
            mchoice = int(input("Enter your choice (1-4): "))
            if mchoice == 1:
                add_staff()
            elif mchoice == 2:
                edit_staff()
            elif mchoice == 3:
                delete_staff()
            elif mchoice == 4:
                break  
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

def add_staff():
    staff_name = input("Enter the staff name: ")
    with open("staff.txt", "a") as file:
        file.write(staff_name + "\n")
    print("Staff name added successfully.")

def edit_staff():
    name_to_edit = input("Enter the staff name to edit: ")

    if not os.path.exists("staff.txt"):
        print("Staff file does not exist.")
        return

    with open("staff.txt", "r") as file:
        staff_list = file.readlines()

    found = False
    with open("staff.txt", "w") as file:
        for line in staff_list:
            if line.strip() == name_to_edit:
                new_name = input("Enter the new name: ")
                file.write(new_name + "\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Staff name updated successfully.")
    else:
        print("Name not found.")

def delete_staff():
    name_to_delete = input("Enter the staff name to delete: ")

    if not os.path.exists("staff.txt"):
        print("Staff file does not exist.")
        return

    with open("staff.txt", "r") as file:
        staff_list = file.readlines()

    with open("staff.txt", "w") as file:
        updated_list = [line for line in staff_list if line.strip() != name_to_delete]

    if len(updated_list) < len(staff_list):
        with open("staff.txt", "w") as file:
            file.writelines(updated_list)
        print("Staff name deleted successfully.")
    else:
        print("Name not found.")

def view_sales():
    if os.path.exists("sales.txt"):
        with open("sales.txt", "r") as file:
            print("\nSales Data:")
            print(file.read())
    else:
        print("Sales file not found.")

def view_feedback():
    if os.path.exists("feedback.txt"):
        with open("feedback.txt", "r") as file:
            print("\nCustomer Feedback:")
            print(file.read())
    else:
        print("Feedback file not found.")

def update_own_profile():
    while True:   
       try:
           m= int(input("Enter the number 1 to continue. \nEnter the number 2 to go back. \nEnter a number: "))
           if m==1:
             name = input("Enter your new name: ")
             email = input("Enter your new email: ")
             password = input("Enter your new password: ")
           
             with open("login_detail.txt", "w") as file:
              file.write(f"\nName: {name}\nEmail: {email}\nPassword: {password}\n")

             print("Profile updated successfully.")
             break

           elif m == 2: 
               break
           else:
               print("Invalid input, Enter the number between 1 or 2")
            
       except ValueError:
           print("Invalid input. Please enter a valid number. ")
       except Exception as f:
           print(f"An error occured: {f}")


login()







