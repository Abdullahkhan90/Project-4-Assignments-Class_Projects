
PLANET_GRAVITIES = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}

def main():
    # Get the user's weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Get the planet name
    planet = input("Enter a planet: ")

    # Check if the planet is valid
    if planet in PLANET_GRAVITIES:
        # Calculate the equivalent weight on the selected planet
        planet_weight = earth_weight * PLANET_GRAVITIES[planet]
        
        # Print the result rounded to two decimal places
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

if __name__ == "__main__":
    main()
