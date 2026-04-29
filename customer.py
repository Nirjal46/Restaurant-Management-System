import os
from utils import load_orders, save_orders, load_feedbacks, save_feedbacks, load_menu, load_customers, save_customers

def customer_menu(customer):
    while True:
        print("\nCustomer Menu:")
        print("1. Check & Order Food")
        print("2. Check Order Status")
        print("3. Submit Feedback")
        print("4. Modify Profile")
        print("5. Logout")
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            place_food_order(customer)
        elif choice == "2":
            check_orders(customer)
        elif choice == "3":
            submit_feedback(customer)
        elif choice == "4":
            modify_profile(customer)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Not valid choice. Please, Try again.")

def place_food_order(customer):
    while True:
        print("\nOrder Menu:")
        print("1. Place Order")
        print("2. Correct Order")
        print("3. Cancel Order")
        print("4. Return")
        sub_choice = input("Select an option: ").strip()
        if sub_choice == "1":
            place_order(customer)
        elif sub_choice == "2":
            correct_order(customer)
        elif sub_choice == "3":
            cancel_order(customer)
        elif sub_choice == "4":
            break
        else:
            print("Not valid choice. Please, Try again.")

def place_order(customer):
    menu = load_menu()
    print("\nAvailable Menu:")
    for category, items in menu.items():
        print(f"{category}:")
        for item, price in items.items():
            print(f"  {item} - ${price}")
    item = input("Enter the item you want to order: ").strip()
    quantity = input("Enter quantity: ").strip()
    if item and quantity.isdigit():
        orders = load_orders()
        price = None
        for cat, items in menu.items():
            if item in items:
                price = items[item]
                break
        if price is None:
            print("Item not available in the menu.")
            return
        orders.append({"customer": customer, "item": item, "quantity": int(quantity), "price": price, "status": "Pending"})
        save_orders(orders)
        print("Order placed successfully.")
    else:
        print("Not valid input. Order not placed.")

def correct_order(customer):
    orders = load_orders()
    customer_orders = [order for order in orders if order["customer"] == customer]
    if not customer_orders:
        print("No orders available to correct.")
        return
    print("\nYour Orders:")
    for idx, order in enumerate(customer_orders, 1):
        print(f"{idx}. {order['item']} (Quantity: {order['quantity']}) - Status: {order['status']}")
    index = input("Enter the order number to edit: ").strip()
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(customer_orders):
            new_quantity = input("Enter new quantity: ").strip()
            if new_quantity.isdigit():
                for order in orders:
                    if order["customer"] == customer and order["item"] == customer_orders[index]["item"]:
                        order["quantity"] = int(new_quantity)
                        break
                save_orders(orders)
                print("Order modified successfully.")
            else:
                print("Not valid quantity.")
        else:
            print("Not valid order number.")
    else:
        print("Not valid input.")

def cancel_order(customer):
    orders = load_orders()
    customer_orders = [order for order in orders if order["customer"] == customer]
    if not customer_orders:
        print("No orders placed to cancel.")
        return
    print("\nYour Orders:")
    for idx, order in enumerate(customer_orders, 1):
        print(f"{idx}. {order['item']} (Quantity: {order['quantity']}) - Status: {order['status']}")
    index = input("Enter the order number to delete: ").strip()
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(customer_orders):
            order_to_delete = customer_orders[index]
            orders = [order for order in orders if not (order["customer"] == customer and order["item"] == order_to_delete["item"])]
            save_orders(orders)
            print("Order canceled successfully.")
        else:
            print("Not valid order number.")
    else:
        print("Not valid input.")

def check_orders(customer):
    orders = load_orders()
    customer_orders = [order for order in orders if order["customer"] == customer]
    if not customer_orders:
        print("No orders submitted yet.")
        return
    print("\nYour Orders:")
    for idx, order in enumerate(customer_orders, 1):
        print(f"{idx}. {order['item']} (Quantity: {order['quantity']}) - Status: {order['status']}")

def submit_feedback(customer):
    feedback = input("Enter your feedback: ").strip()
    if feedback:
        feedbacks = load_feedbacks()
        if customer not in feedbacks:
            feedbacks[customer] = []
        feedbacks[customer].append(feedback)
        save_feedbacks(feedbacks)
        print("Feedback submitted successfully.")
    else:
        print("Feedback box cannot be empty.")

def modify_profile(customer):
    customers = load_customers()
    if customer in customers:
        new_email = input("Enter new email (or press Enter to keep current): ").strip()
        new_password = input("Enter new password (or press Enter to keep current): ").strip()
        if new_email:
            customers[customer]["email"] = new_email
        if new_password:
            customers[customer]["password"] = new_password
        save_customers(customers)
        print("Profile modified successfully.")
    else:
        print("Profile not available.")

if __name__ == "__main__":
    customer = "customer@example.com"  
    customer_menu(customer)
