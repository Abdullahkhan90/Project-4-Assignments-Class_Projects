# Step 1: Import the math module to use the sqrt function
import math  # The math module will help us calculate the square root

# Step 2: Define the main function
def main():
    # Step 3: Get the lengths of the two perpendicular sides from the user
    ab = float(input("Enter the length of AB: "))  # Length of side AB (one perpendicular side)
    ac = float(input("Enter the length of AC: "))  # Length of side AC (the other perpendicular side)

    # Step 4: Calculate the length of the hypotenuse (BC) using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)  # Apply the formula BC^2 = AB^2 + AC^2, and take the square root
    
    # Step 5: Output the result
    print("The length of BC (the hypotenuse) is: " + str(bc))  # Display the length of the hypotenuse

# Step 6: Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()
