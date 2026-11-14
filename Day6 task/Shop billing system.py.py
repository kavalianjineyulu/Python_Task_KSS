# Small Shop Billing System

# Dictionary: Product names and prices
products = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 150,
    "Milk": 30,
    "Soap": 40
}

# Set: Product categories
categories = {"Grocery", "Food", "Household"}

# Tuple: Product details
product_details = (
    ("Rice", "Grocery"),
    ("Sugar", "Grocery"),
    ("Oil", "Food"),
    ("Milk", "Food"),
    ("Soap", "Household")
)

# List: Shopping cart
cart = []


# Function to display products
def display_products():
    print("\nAvailable Products:")
    for name, price in products.items():
        print(name, ":", price)


# Function to add items to cart
def add_to_cart():
    try:
        name = input("\nEnter product name: ").title()

        if name not in products:
            raise NameError("Product does not exist!")

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")

        price = products[name]

        cart.append((name, price, quantity))

        print("Product added successfully!")

    except ValueError:
        print("Error: Please enter a valid quantity.")

    except NameError as e:
        print("Error:", e)


# Recursive function to calculate total
def calculate_total(index=0):
    if index == len(cart):
        return 0

    name, price, quantity = cart[index]

    return (price * quantity) + calculate_total(index + 1)


# Function to display bill
def display_bill():
    try:
        if not cart:
            print("\nCart is empty!")
            return

        print("\n========== CUSTOMER BILL ==========")

        for name, price, quantity in cart:
            print(name, "Price:", price,
                  "Quantity:", quantity,
                  "Total:", price * quantity)

        total = calculate_total()

        print("-----------------------------------")
        print("Total Bill Amount:", total)
        print("Thank you for shopping!")

    except TypeError:
        print("Error: Wrong data type in cart.")

    except ZeroDivisionError:
        print("Error: Division by zero occurred.")


# Main program
while True:

    print("\n===== SMALL SHOP BILLING SYSTEM =====")
    print("1. Display Products")
    print("2. Add Items to Cart")
    print("3. Calculate Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            display_bill()

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter numbers only.")
