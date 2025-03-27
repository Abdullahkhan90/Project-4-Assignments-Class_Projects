def main():
    # Step 2: Create a dictionary of fruits with their prices
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    # Step 3: Initialize the total cost variable
    total_cost = 0
    
    # Step 4: Loop through the fruits dictionary to get the quantity from the user and calculate the total cost
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    # Step 5: Print the total cost
    print("Your total is $" + str(total_cost))

# Step 6: Ensure the main function is called
if __name__ == '__main__':
    main()
