import os

def manager_menu():
    while True:
        print("\nPlease select an option from 1-5: ")
        print("1. Manage customer")
        print("2. Manage menu")
        print("3. View ingredients")
        print("4. Update own profile")
        print("5. Logout")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                manage_customer()
            elif choice == 2:
                manage_menu()
            elif choice == 3:
                view_ingredient()
            elif choice == 4:
                update_own_profile()
            elif choice == 5:
                print("Logging out...\n")
                break  
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")

def manage_customer():
    while True:
        print("\nManage Customer:")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. Go Back")

        try:
            mchoice = int(input("Enter your choice (1-4): "))
            if mchoice == 1:
                add_customer()
            elif mchoice == 2:
                edit_customer()
            elif mchoice == 3:
                delete_customer()
            elif mchoice == 4:
                break  
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

def add_customer():
    customer_name = input("Enter the customer name: ")
    with open("customer.txt", "a") as file:
        file.write(customer_name + "\n")
    print("Customer name added successfully.")


def edit_customer():
    name_to_edit = input("Enter the customer name to edit: ")

    if not os.path.exists("customer.txt"):
        print("Customer file does not exist.")
        return

    with open("customer.txt", "r") as file:
        customer_list = file.readlines()

    found = False
    with open("customer.txt", "w") as file:
        for line in customer_list:
            if line.strip() == name_to_edit:
                new_name = input("Enter the new name: ")
                file.write(new_name + "\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Customer name updated successfully.")
    else:
        print("Name not found.")
def manage_menu():
    while True:
        print("\nManage Menu:")
        print("1. Add Menu Item")
        print("2. Edit Menu Item")
        print("3. Delete Menu Item")
        print("4. Go Back")

        try:
            mchoice = int(input("Enter your choice (1-4): "))
            if mchoice == 1:
                add_menu_item()
            elif mchoice == 2:
                edit_menu_item()
            elif mchoice == 3:
                delete_menu_item()
            elif mchoice == 4:
                break  
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

def add_menu_item():
    item_name = input("Enter the item: ")
    price=int(input(f"Enter the price for {item_name}:  "))
    with open("menu.txt", "a") as file:
        file.write(item_name+"\t" )
        file.write( str(price) + "\n")
    print("Item added successfully.")

def edit_menu_item():
    item_to_edit = input("Enter the item to edit: ")

    if not os.path.exists("menu.txt"):
        print("Item file does not exist.")
        return

    with open("menu.txt", "r") as file:
        item_list = file.readlines()

    found = False
    with open("menu.txt", "w") as file:
        for line in item_list:
            if line.strip() == item_to_edit:
                new_item = input("Enter the new item: ")
                file.write(new_item + "\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Item updated successfully.")
    else:
        print("Item not found.")
def delete_menu_item():
    item_to_delete = input("Enter the item name to delete: ")

    if not os.path.exists("menu.txt"):
        print("Item does not exist.")
        return

    with open("menu.txt", "r") as file:
        item_list = file.readlines()

    with open("menu.txt", "w") as file:
        updated_list = [line for line in item_list if line.strip() != item_to_delete]

    if len(updated_list) < len(item_list):
        with open("menu.txt", "w") as file:
            file.writelines(updated_list)
        print("Item deleted successfully.")
    else:
        print("Item not found.")

def delete_customer():
    name_to_delete = input("Enter the customer name to delete: ")

    if not os.path.exists("customer.txt"):
        print("Customer file does not exist.")
        return

    with open("customer.txt", "r") as file:
        customer_list = file.readlines()

    updated_list = [line for line in customer_list if line.strip() != name_to_delete]

    if len(updated_list) < len(customer_list):
        with open("customer.txt", "w") as file:
            file.writelines(updated_list)
        print("Customer name deleted successfully.")
    else:
        print("Name not found.")

def view_ingredient():
    if os.path.exists("ingredients.txt"):
        with open("ingredients.txt", "r") as file:
            print("\nIngredient Data:")
            print(file.read())
    else:
        print("Ingredient file not found.")

def update_own_profile():
    while True:   
       try:
           m = int(input("Enter the number 1 to continue. \nEnter the number 2 to go back. \nEnter a number: "))
           if m == 1:
               name = input("Enter your new name: ")
               email = input("Enter your new email: ")
               password = input("Enter your new password: ")
           
               with open("login_information.txt", "w") as file:
                   file.write(f"\nName: {name}\nEmail: {email}\nPassword: {password}\n")

               print("Profile updated successfully.")
               break

           elif m == 2: 
               break
           else:
               print("Invalid input, Enter the number between 1 or 2")
            
       except ValueError:
           print("Invalid input. Please enter a valid number.")
       except Exception as f:
           print(f"An error occurred: {f}")
