def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  
    
    while True:
        name = input("Name: ")
        if name == "":
            break  # Exit the loop when the user enters an empty string
        
        number = input("Number: ")
        phonebook[name] = number  # Add name and number to the phonebook
    
    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Exit the loop when the user enters an empty string
        
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])  # Print the number associated with the name

def main():
    """
    Coordinates the phonebook operations: reading numbers, printing the phonebook, and allowing lookups.
    """
    phonebook = read_phone_numbers()  
    print_phonebook(phonebook)         
    lookup_numbers(phonebook)         


if __name__ == '__main__':
    main()
