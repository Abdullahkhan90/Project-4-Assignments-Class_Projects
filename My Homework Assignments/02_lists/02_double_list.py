# Step 1: Define the main function
def main():
    # Step 2: Create a list of numbers
    numbers: list[int] = [1, 2, 3, 4]  # This is the original list of numbers

    # Step 3: Loop through each index of the list
    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Double the element at index i and update the list

    # Step 4: Print the updated list
    print(numbers)  # This will print the list with each element doubled

# Step 5: Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()
