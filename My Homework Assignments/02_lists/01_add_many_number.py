# Step 1: Define the function to calculate the sum of numbers
def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    # Step 2: Initialize a variable to hold the running total of the sum
    total_so_far: int = 0
    
    # Step 3: Iterate through each number in the list and add it to the total
    for number in numbers:
        total_so_far += number

    # Step 4: Return the final sum
    return total_so_far

# Step 5: Define the main function to call the add_many_numbers function
def main():
    # Step 6: Create a list of numbers
    numbers: list[int] = [1, 2, 3, 4, 5]  # Example list of numbers
    
    # Step 7: Call the function to get the sum of the numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    
    # Step 8: Print the result
    print(sum_of_numbers)  # Output the sum of the numbers

# Step 9: Ensure that the main function is called when the script is executed
if __name__ == '__main__':
    main()
