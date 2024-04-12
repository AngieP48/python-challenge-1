# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items_display = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
             # Check if the menu item is a dictionary to handle differently
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items_display[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                        
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items_display[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_items_selection = input("Type menu item number: ")

            # 3. Check if the customer typed a number
            if menu_items_selection.isdigit():
                print(f"Menu item number selected")
                menu_selection =  int(menu_items_selection)
                print("Menu Selection", menu_selection)
                if menu_selection in menu_items.keys():
                    print(f"Menu selection is selected")
                    menu_selection =  int(menu_selection)
                    print("Menu Selection", menu_selection)
                    menu_items[menu_selection]
                    quantity = input(f"Please enter the quantity of the menu item")
                    if quantity.isdigit():
                        quantity = int(quantity)
                        print("Quantity stored", quantity)
                        try:
                            quantity = int(quantity)
                        except ValueError:
                            print("Invalid input. Defaulting quantity to 1.")
                            quantity = 1

            else:
                print("Invalid input. Please enter a valid number.")

                # Convert the menu selection to an intege

                # 4. Check if the menu selection is in the menu items     
                    
                    # Store the item name as a variable
                    
                    # Ask the customer for the quantity of the menu ite

                    # Check if the quantity is a number, default to 1 if not

                    # Add the item name, price, and quantity to the order list
                order_list = []
                    
                item_details = {
                    "Item name": item_name,
                    "Price": price,
                    "Quantity": quantity
                    }
                order_list.append(item_details)

                print("Order list after adding the item:")
                print("order_list", list)

                    # Tell the customer that their input isn't valid
                print("Invalid input. Please try again.")

                # Tell the customer they didn't select a menu option
                print("Oops! You have not select a menu option. Please try again")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You did not select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering
        if keep_ordering.lower() == 'y':
            place_order = True
            break
        elif keep_ordering.lower() == 'n':
            place_order = False
            print("You have exit the the ordering process, we hope to see you again!")
            break
        else:
            print("Invalid input. Please try again.")
                
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for order_item in menu: 
    item_name = menu("menu_items")
    price = menu("price")
    quantity = menu("quantity")
    print(f"Item: {item_name}, Price: ${price}, Quantity: {quantity}")

    # 7. Store the dictionary items as variables

    # 8. Calculate the number of spaces for formatted printing
total_width = 20
num_item_spaces = total_width - len(key) - len(value)
 
    # 9. Create space strings
item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
print(f"{item_name.ljust(25)} | ${price:.2f} | {quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
item_total = sum(price * quantity)
total_cost = sum(price)
print("Total Cost of the order: ${total_cost:.2f}")