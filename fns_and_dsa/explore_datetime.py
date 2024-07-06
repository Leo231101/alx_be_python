# explore_datetime.py
import datetime

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculates and displays the future date after adding a specified number of days.
    """
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=num_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

