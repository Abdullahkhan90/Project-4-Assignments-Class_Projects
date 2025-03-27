MAX_TERM_VALUE = 10000  

def main():
    curr_term = 0  
    next_term = 1  
    
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current term, and separate them by space
        term_after_next = curr_term + next_term  # Calculate the next Fibonacci number
        curr_term = next_term  # Update the current term
        next_term = term_after_next  # Update the next term

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
