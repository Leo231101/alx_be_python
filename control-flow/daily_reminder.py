# daily_reminder.py

def main():
    # Prompt the user to enter a task description
    task = input("Enter your task: ")

    # Prompt the user to enter the task's priority
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt the user to enter if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Use a match case statement to handle different priority levels
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            reminder = f"'{task}' has an unknown priority level."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."

    # Print the customized reminder
    print(f"Reminder: {reminder}")

# Ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()

