def main():
    # Prompt the user for the temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert the temperature to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
