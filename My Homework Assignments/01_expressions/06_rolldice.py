
import random  


NUM_SIDES = 6  # A standard die has 6 sides

def main():
  
    die1 = random.randint(1, NUM_SIDES)  
    die2 = random.randint(1, NUM_SIDES)  
    

    total = die1 + die2  
    
    
    print("Dice have", NUM_SIDES, "sides each.")  # Inform the user about the number of sides on each die
    print("First die:", die1)  # Display the result of the first die
    print("Second die:", die2)  # Display the result of the second die
    print("Total of two dice:", total)  # Display the total of both dice rolls
if __name__ == '__main__':
    main()
