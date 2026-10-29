"""Week 8: menu and file handling for the object-oriented inventory system."""

import json
import math
from pathlib import Path

from inventory import Inventory
from product import Product


# Keep the data beside this script, including when launched from VS Code.
INVENTORY_FILE = Path(__file__).resolve().with_name("inventory.json")


def load_inventory(filename=INVENTORY_FILE):
    inventory = Inventory()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return inventory

    if not isinstance(data, list):
        raise ValueError("Inventory data must be a list of products.")
    for record in data:
        if not isinstance(record, dict):
            raise ValueError("Each inventory entry must be a product record.")
        inventory.add_product(Product(
            record["id"], record["name"], record["price"], record["stock"]
        ))

    print("inventory.json found.")
    print("Inventory loaded successfully.")
    return inventory


def save_inventory(inventory, filename=INVENTORY_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(inventory.to_list(), file, indent=4, allow_nan=False)
    print("Inventory saved successfully to inventory.json.")


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")


def read_price():
    while True:
        try:
            price = float(input("Price: "))
            if math.isfinite(price) and price >= 0:
                return price
        except ValueError:
            pass
        print("Error: Please enter a finite, non-negative price.")


def read_stock(prompt):
    while True:
        try:
            stock = int(input(prompt))
            if stock >= 0:
                return stock
        except ValueError:
            pass
        print("Error: Please enter a non-negative whole number.")


def add_product(inventory):
    print("\nAdd New Product")
    product_id = read_text("Product ID: ").upper()
    if inventory.search_product(product_id) is not None:
        print("Error: A product with this ID already exists.")
        return
    name = read_text("Product Name: ")
    price = read_price()
    stock = read_stock("Stock Quantity: ")
    inventory.add_product(Product(product_id, name, price, stock))
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    product.display_information()
    quantity = read_stock("New Stock Quantity: ")
    inventory.update_stock(product_id, quantity)
    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    try:
        inventory = load_inventory()
    except (OSError, ValueError, KeyError, TypeError) as error:
        # Do not replace an unreadable data file with an empty inventory.
        print(f"Unable to load inventory: {error}")
        print("Please fix inventory.json before running the program again.")
        return

    while True:
        display_menu()
        option = input("Enter option: ").strip()
        if option == "1":
            inventory.display_all()
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option in ("5", "6"):
            try:
                save_inventory(inventory)
            except OSError as error:
                print(f"Unable to save inventory: {error}")
                continue
            if option == "6":
                print("Thank you for using Inventory Management System.")
                print("Program terminated.")
                break
        else:
            print("Error: Please enter an option from 1 to 6.")


if __name__ == "__main__":
    main()
