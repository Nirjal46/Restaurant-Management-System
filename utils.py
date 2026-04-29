import json
import os

# File paths for data storage
orders_file = "orders.json"
feedbacks_file = "feedbacks.json"
menu_file = "menu.json"
customers_file = "customers.json"


def load_orders():
    if os.path.exists(orders_file):
        with open(orders_file, 'r') as f:
            return json.load(f)
    return []


def save_orders(orders):
    with open(orders_file, 'w') as f:
        json.dump(orders, f, indent=4)


def load_feedbacks():
    if os.path.exists(feedbacks_file):
        with open(feedbacks_file, 'r') as f:
            return json.load(f)
    return {}


def save_feedbacks(feedbacks):
    with open(feedbacks_file, 'w') as f:
        json.dump(feedbacks, f, indent=4)


def load_menu():
    if os.path.exists(menu_file):
        with open(menu_file, 'r') as f:
            return json.load(f)
    return {}  


def load_customers():
    if os.path.exists(customers_file):
        with open(customers_file, 'r') as f:
            return json.load(f)
    return {}  
def save_customers(customers):
    with open(customers_file, 'w') as f:
        json.dump(customers, f, indent=4)
