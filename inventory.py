"""Inventory Manager - a command-line application to manage products.

A product is a dict with 4 attributes: name, quantity, category and price.
"""


class ProductNotFoundError(Exception):
    """Raised when an operation targets a product that does not exist."""


class ProductAlreadyExistsError(Exception):
    """Raised when adding a product whose name is already in the inventory."""


def create_inventory():
    return []


def find_product(inventory, name):
    for product in inventory:
        if product["name"] == name:
            return product
    return None


def add_product(inventory, name, quantity, category, price):
    if find_product(inventory, name) is not None:
        raise ProductAlreadyExistsError(f'Product "{name}" already exists')
    product = {
        "name": name,
        "quantity": quantity,
        "category": category,
        "price": price,
    }
    inventory.append(product)
    return product


def list_products(inventory):
    return list(inventory)


def update_quantity(inventory, name, quantity):
    product = find_product(inventory, name)
    if product is None:
        raise ProductNotFoundError(f'Product "{name}" not found')
    product["quantity"] = quantity
    return product


def remove_product(inventory, name):
    product = find_product(inventory, name)
    if product is None:
        raise ProductNotFoundError(f'Product "{name}" not found')
    inventory.remove(product)
    return product


def search_by_category(inventory, category):
    """5th feature: search products that belong to a given category."""
    return [product for product in inventory if product["category"] == category]


def format_inventory(inventory):
    lines = ["Products:"]
    lines.extend(f"- {product['name']}" for product in inventory)
    return "\n".join(lines)


MENU = """
Inventory Manager
1. Add product
2. List products
3. Update quantity
4. Remove product
5. Search by category
0. Exit
"""


def run_cli():
    inventory = create_inventory()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                name = input("Name: ").strip()
                quantity = int(input("Quantity: ").strip())
                category = input("Category: ").strip()
                price = float(input("Price: ").strip())
                add_product(inventory, name, quantity, category, price)
                print(f'Product "{name}" added.')
            elif choice == "2":
                print(format_inventory(list_products(inventory)))
            elif choice == "3":
                name = input("Name: ").strip()
                quantity = int(input("New quantity: ").strip())
                update_quantity(inventory, name, quantity)
                print(f'Product "{name}" updated to quantity {quantity}.')
            elif choice == "4":
                name = input("Name: ").strip()
                remove_product(inventory, name)
                print(f'Product "{name}" removed.')
            elif choice == "5":
                category = input("Category: ").strip()
                results = search_by_category(inventory, category)
                print(format_inventory(results))
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid option.")
        except (ProductNotFoundError, ProductAlreadyExistsError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    run_cli()
