
#Tuple for items
grocery_items = (
    "Grape",
    "Banana",
    "Tangerine",
    "Mango",
    "watermelon"
)
#tuple for Prices
grocery_prices = (25,15,10,20,)

total_cost = 0

#super Loop For main
while True:
    print("\nWelcome to MyGroceryShop!")
    print("Grocery items available:")
    for i in range(len(grocery_items)):
        print(f"{i+1}. {grocery_items[i]} (${grocery_prices[i]:.2f})")
    print("Enter 'done' to exit.")

    item_choice = input("Enter item choice: ")

    if item_choice == "done":
        print(f"Total cost: LE{total_cost:.2f}")
        print("Thank you for shopping with us!")
        break

    item_choice_valid = True
    for char in item_choice:
        if not char.isdigit():
            item_choice_valid = False
            break

    if not item_choice_valid:
        print("Invalid item choice. Please try again.")
        continue

    item_choice = int(item_choice)
    if item_choice < 1 or item_choice > len(grocery_items):
        print("Invalid item choice. Please try again.")
        continue

    item_index = item_choice - 1
    item_price = grocery_prices[item_index]
    total_cost += item_price
    print(f"{grocery_items[item_index]} added to cart. Cost: LE{item_price:.2f}. Total cost: LE{total_cost:.2f}")