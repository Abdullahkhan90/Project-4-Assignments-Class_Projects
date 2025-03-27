
def main():
    # Step 2: Ask the user for the first number (dividend)
    dividend = int(input("Please enter an integer to be divided: "))  # Get the number to be divided
    
    # Step 3: Ask the user for the second number (divisor)
    divisor = int(input("Please enter an integer to divide by: "))  # Get the number to divide by

    # Step 4: Perform the division and calculate the quotient and remainder
    quotient = dividend // divisor  # Integer division to get the quotient (result without decimals)
    remainder = dividend % divisor  # Modulo operation to get the remainder

    # Step 5: Output the result to the user
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# Step 6: Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()
    
