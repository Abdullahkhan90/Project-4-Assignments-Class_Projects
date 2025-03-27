# Step 1: Define the constant speed of light (C)
C = 299792458  # Speed of light in meters per second

# Step 2: Define the main function
def main():
    # Step 3: Get the mass input from the user
    mass_in_kg = float(input("Enter kilos of mass: "))  # Take input and convert it to float
    
    # Step 4: Calculate the energy using Einstein's formula (E = m * C^2)
    energy_in_joules = mass_in_kg * (C ** 2)  # Apply the formula
    
    # Step 5: Display the calculations and results
    print("e = m * C^2...")  # Display the formula
    print("m = " + str(mass_in_kg) + " kg")  # Show mass
    print("C = " + str(C) + " m/s")  # Show speed of light
    print(str(energy_in_joules) + " joules of energy!")  # Show the calculated energy

# Step 6: Ensure that main() runs when the program is executed
if __name__ == '__main__':
    main()
