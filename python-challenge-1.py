# Interacting Operation with Food Truck
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

menu_item_name = [Cookie, Banana, Apple, Granola bar, Burrito, Teriyaki Chicken, Sushi, Pad Thai, Cheese, 
                  Pepperoni, Vegetarian, Chicken, Beef, Small, Medium, Large, Green, Thai iced, Irish breakfast, 
                  Espresso, Flat White, Iced, Chocolate lava cake, New York, Strawberry, Australian Pavlova, Rice pudding, Fried banana]
item_price = [.99, .69, .49, 1.99, 4.49, 9.99, 7.49, 9.99, 7.49, 6.99, 8.99, 10.99, 9.99,
              7.49, 8.49, 1.99, 2.49, 2.99, 2.49, 2.99, 2.49, 3.99, 2.49, 2.99, 2.99, 3.49, 10.99, 4.99, 6.49,
              9.99, 4.99, 4.49]
quantity_ordered = []


print("Welcome to the variety food truck.")

place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
    menu_items[i] = key
    i += 1

menu_category = input("Type menu number: ")

if menu_category.isdigit():
    if int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")
        print(f"What {menu-menu_category_name} item would you like to order?")
        i = 1
        menu_items = {}
        print("Item # | Item Name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if type(value) is dict
                for key2,value2 in value.items():
                    num_item_spaces = 24 -len(key +key2) - 3
                    items_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {
                        "Item name": key + " - " + key2,
                        "Price": value2
                        }
                    i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                # 2. Ask customer to input menu item number
            menu_items = input("Type menu item number:")

            # 3. Check if the customer typed a number
            if menu_items.isdigit(): 
                print("The input is a number.")
            else:
                print("The input is not a number.")

                # Convert the menu selection to an integer
                menu_selection = input("Please enter your menu selection: ")
                try:
                    menu_selection = int(menu_selection)
                    print("Menu selection converted to integer successfully:", menu_selection)
                except ValueError:
                     print("Error: Menu selection must be a number.")

                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable
                    item_name = input("Please enter the item name": )
                        print("Item name stored:", item_name)

                    # Ask the customer for the quantity of the menu item
                    quantity = input("Please enter the quantity of the menu item": )
                    if quantity.isdigit():
                        quantity = int(quantity)
                        print("Queantity entered:", quantity)
                    else: 
                        quantity = 1
                        print("invalid input. Quantity set to default value of 1.")

                    # Check if the quantity is a number, default to 1 if not
                        


                    # Add the item name, price, and quantity to the order list
                    order_list = []
                    item_name = "Fruit Bowl"
                    price = 2.99
                    quantity = 2
                
                    "Fruit Bowl": item_name
                    "2.99":  price,
                    "2": quantity
                
                    order_list.append(order.item)
                    print(order_list)
                

                    # Tell the customer that their input isn't valid
                    print("Invalid input. Please try again.")

                # Tell the customer they didn't select a menu option
                print("Oops! You have not select a menu option. Please try again")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering
                if keep_ordering.lower() == 'y' :
                    print("Right on! Continue ordering!")
                # Exit the keep ordering question loop
                elif keep_ordering.lower() == 'n':
                    print("You have exit the the ordering process, we hope to see you again!")
                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.                      