# Project Title
Simple Shopping Cart System

## Overview of the Project
This Python project simulates a shopping cart system. Users can add items with prices to a cart, view the cart, remove items, and checkout. The program demonstrates basic programming concepts such as functions, lists, loops, and input/output handling. It provides a simple, interactive way to manage a virtual shopping experience.

## Features
- Add items with price to the cart
- View all items and total price
- Remove items from the cart
- Checkout system with final bill
- Exit program option

## Technologies / Tools Used
- Python 3.x
- Any Python IDE or online Python compiler

## Steps to Install & Run the Project
1. Make sure Python 3.x is installed on your computer.
2. Download or copy the project folder containing main.py, statement.md, and this README.md.
3. Open *Command Prompt (Windows)* or *Terminal (Mac/Linux)*.
4. Navigate to the project folder using the cd command. For example:cd Desktop/ShoppingCartProject
5. Run the program by typing: python main.py
6. The program menu will appear. You can now:  
   - Add items to cart  
   - View cart  
   - Remove items  
   - Checkout  

## Instructions for Testing
1. Run the program as described above.
2. Add a few items to the cart (e.g., Apple ₹50, Milk ₹30).
3. View the cart to check that items appear correctly with the total amount.
4. Remove an item and check that it is removed correctly.
5. Checkout to verify the final bill is displayed.

## Algorithm 
1. Start the program and initialize an empty cart list.
2. Display the menu repeatedly:

          1 → Add item to cart

          2 → View cart

          3 → Remove item from cart

          4 → Checkout

          5 → Exit
3. Get user input for menu choice.
4. Process choice:
                  Add Item (1):

                  Ask user for item name and price.

                  Add [item, price] to cart.

                  Display confirmation message.


                  View Cart (2):

                  If cart is empty, display “Your cart is empty.”

                  Else, list all items with their prices and total cost.


                  Remove Item (3):

                  Display cart items with numbers.

                  Ask user for item number to remove.

                  Remove the selected item from cart.

                  Display confirmation message.


                  Checkout (4):

                  Display all cart items and total cost.

                  Display a thank you message.

                  End the program.


                  Exit (5):

                  End the program.
                  
                  Invalid Input:

                  Display “Invalid choice! Please try again.”

5. Repeat steps 2–4 until the user chooses Checkout or Exit.
6. End the program.


## Pseudocode
START
cart = empty list

WHILE True
    DISPLAY menu:
        1. Add item to cart
        2. View cart
        3. Remove item from cart
        4. Checkout
        5. Exit

    GET choice from user

    IF choice == 1
        INPUT item name
        INPUT item price
        ADD [item, price] to cart
        PRINT "Item added to cart"

    ELSE IF choice == 2
        IF cart is empty
            PRINT "Your cart is empty"
        ELSE
            FOR each item in cart
                PRINT item name and price
            PRINT total cost

    ELSE IF choice == 3
        IF cart is empty
            PRINT "Your cart is empty"
        ELSE
            DISPLAY items with numbers
            INPUT item number to remove
            REMOVE selected item from cart
            PRINT "Item removed"

    ELSE IF choice == 4
        DISPLAY items with total
        PRINT "Thank you for shopping!"
        BREAK

    ELSE IF choice == 5
        PRINT "Exiting program"
        BREAK

    ELSE
        PRINT "Invalid choice! Please try again"

END WHILE
END


## Program Screenshot
![Program Screenshot](images/program.png)
























