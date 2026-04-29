from customer import *
c="customer@example.com"
ingredients = []
requested_ingredients = []

def main_menu():
      while True:
        print("1. Orders Received")
        print("2. Manage Ingredients")
        print("3. Update Own Profile")
        print("4. Exit\n")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            check_orders(c)
        elif choice == 2:
            manage_ingredients()
        elif choice == 3:
            update_own_profile()
        elif choice == 4:
            print("Exiting the program....")
            break
        else:
            print("Invalid choice!! Please try again.")

def add_ingredients():
    ingredients = input("Enter the ingredients: ")
    with open("ingredients.txt", "a") as file:
        file.write(ingredients + "\n")
    print("Ingredients added successfully.")


def edit_ingredients():
    ingredients_id_input = input("\nEnter the ingredient id of the igrendient you want to edit: ")
    if not ingredients_id_input.strip():
        print("No ignredients id entered.")
        return
    
    try:
        ingredients_id = int(ingredients_id_input)
    except ValueError:
        print("Invalid input for customer id. Please enter a valid number.")
        return
    
    for a in ingredients:
        if ["ingredients_id"] == ingredients_id:
            print("Editing data:", ingredients)

            new_ingredients_id_input = input("Enter new customer id (press enter to keep current): ")
            if new_ingredients_id_input.strip():
                try:
                   a["ingredients_id"] = int(new_ingredients_id_input)
                except ValueError:
                    print("Invalid input. Keeping the current id.")
        
            new_ingredient = input("Enter name (press enter to keep current): ")
            if new_ingredient.strip():
               a["ingredient"] = new_ingredient
            
            print("Ingredient data updated.")

            f = open("ingredients.txt","w")
            for a in ingredients:
                f.write(f"\nIngredients Id : {a['ingredients_id']}\nIngredient : {a['ingredient']}\n")
            f.close()
            return
    print("Ingredient not found")


def delete_ingredients():
    try:
        ingredients_id = int(input("Enter the ingredients id you want to delete: "))
    except ValueError:
        print("Invalid ingredients id. It must be a number.")
        return

    for a in ingredients:
        if a["ingredients_id"] ==  ingredients_id:
            ingredients.remove(a)
            print("ingredients item deleted.")

            f = open("ingredients.txt", "w")
            for a in ingredients:
                f.write(f"\nIngredients id: {a['ingredients_id']}\nIngredient: {a['ingredient']}")
            f.close()
            return
    print("ingredients not found.")
    

def request_ingredients():
    req_ingredients = input("Enter the ingredients you need:")
    requested_ingredients.append(req_ingredients)

    f = open("req_ingredients.txt", "a+")
    f.write(f"{req_ingredients}\n")
    f.close()
    return


def view_ingredients():
    f = open("ingredients.txt")
    print("List of ingredients::")
    print(f.read())
    f.close()
    return


def manage_ingredients():
    while True:
        print("\n\n1. Add Ingredients")
        print("2. Edit Ingredients")
        print("3. Delete Ingredients")
        print("4. Request Ingredients")
        print("5. View Ingredients")
        print("6. Exit\n")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            add_ingredients()
        elif choice == 2:
            edit_ingredients()
        elif choice == 3:
            delete_ingredients()
        elif choice == 4:
            request_ingredients()
        elif choice == 5:
            view_ingredients()
        elif choice == 6:
            print("Exiting the program....")
            break
        else:
            print("Invalid choice!! Please try again.")

def update_own_profile():
    while True:   
       try:
           m= int(input("Enter the number 1 to continue. \nEnter the number 2 to go back. \nEnter a number: "))
           if m==1:
             name = input("Enter your new name: ")
             email = input("Enter your new email: ")
             password = input("Enter your new password: ")
           
             with open("login_information_x.txt", "w") as file:
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

if __name__ == "__main__":
    main_menu()
