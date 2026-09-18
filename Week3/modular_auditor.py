def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

        if user_input.lower() == "quit":
            return "quit"

        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Negative stock values are not allowed.")
            return None

        if not user_input.isdigit():
            print("Error: Invalid entry. Please enter a positive whole number.")
            return None

        return int(user_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts, deliveries_processed):
    print("\n--- Inventory Audit Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


# Initialise inventory and counters
total_inventory = 0
rejected_count = 0
deliveries_processed = 0

while True:
    quantity = get_valid_input()

    if quantity == "quit":
        break

    if quantity is None:
        rejected_count += 1
        continue

    total_inventory = process_delivery(total_inventory, quantity)
    tax = calculate_tax(quantity)
    deliveries_processed += 1

    print(f"Accepted {quantity} units.")
    print(f"Tax for this delivery: {tax:.2f}")
    print(f"Current Total: {total_inventory}")

generate_report(total_inventory, rejected_count, deliveries_processed)