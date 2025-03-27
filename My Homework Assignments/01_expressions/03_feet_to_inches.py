# Step 1: Define the constant for the number of inches in one foot
INCHES_IN_FOOT = 12  # There are 12 inches in 1 foot

# Step 2: Define the main function
def main():
    # Step 3: Get the number of feet as input from the user
    feet = float(input("Enter number of feet: "))  # Convert the input to float
    
    # Step 4: Convert feet to inches by multiplying with the constant
    inches = feet * INCHES_IN_FOOT  # Perform the conversion
    
    # Step 5: Display the result to the user
    print("That is", inches, "inches!")  # Output the result in inches

# Step 6: Ensure that the main() function is called when the script is executed
if __name__ == '__main__':
    main()
