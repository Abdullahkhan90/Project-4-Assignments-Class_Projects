def access_element(my_list, index):
    # Check if the index is in range
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

def modify_element(my_list, index, new_value):
    # Check if the index is in range
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return my_list
    else:
        return "Index out of range."

def slice_list(my_list, start_index, end_index):
    # Check if the indices are in range
    if 0 <= start_index < len(my_list) and 0 <= end_index <= len(my_list):
        return my_list[start_index:end_index]
    else:
        return "Index out of range."

def main():
    # Create a list with 5 elements
    my_list = [10, 'apple', 3.14, 'banana', 42]
    
    # Start the game
    print("Welcome to the Index Game!")
    
    while True:
        # Ask the user for an operation
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        operation = input("Enter the number of the operation (1-4): ")
        
        if operation == '1':
            index = int(input("Enter the index you want to access: "))
            result = access_element(my_list, index)
            print(f"Accessed element: {result}")
        
        elif operation == '2':
            index = int(input("Enter the index you want to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(f"Updated list: {result}")
        
        elif operation == '3':
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            result = slice_list(my_list, start_index, end_index)
            print(f"Sliced list: {result}")
        
        elif operation == '4':
            print("Thanks for playing!")
            break  # Exit the loop and end the game
        
        else:
            print("Invalid option. Please select a valid operation.")

# Run the game
if __name__ == "__main__":
    main()
