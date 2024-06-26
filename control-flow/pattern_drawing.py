# pattern_drawing.py

def main():
    try:
        # Prompt the user to enter a positive integer for the size of the pattern
        size = int(input("Enter the size of the pattern: "))
        
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        # Initialize the row counter
        row = 0
        
        # Use a while loop to iterate through each row of the pattern
        while row < size:
            # Use a for loop to print asterisks side by side
            for col in range(size):
                print("*", end="")
            # Print a newline character to move to the next row
            print()
            # Increment the row counter
            row += 1
            
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# Ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()
