# Simple Shopping Cart System

cart = []  # Empty cart list

def show_menu():
    print("\n--- SHOPPING MENU ---")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Checkout")
    print("5. Exit")

def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart.append([item, price])
    print(f"{item} added to cart!")

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\n--- YOUR CART ---")
        total = 0
        for i, (item, price) in enumerate(cart, 1):
            print(f"{i}. {item} - ₹{price}")
            total += price
        print(f"Total amount: ₹{total}")

def remove_item():
    view_cart()
    if cart:
        index = int(input("Enter item number to remove: "))
        if 1 <= index <= len(cart):
            removed = cart.pop(index - 1)
            print(f"{removed[0]} removed from cart.")
        else:
            print("Invalid choice.")

def checkout():
    view_cart()
    print("\nThank you for shopping! Your order is placed.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        checkout()
        break
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
