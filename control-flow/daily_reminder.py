# Prompt the user for a task description
task = input("Enter a task description: ")

# Prompt the user for the task's priority
priority = input("Enter the priority of the task (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is this task time-sensitive? (yes/no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        reminder = f"Your task '{task}' has a high priority."
    case "medium":
        reminder = f"Your task '{task}' has a medium priority."
    case "low":
        reminder = f"Your task '{task}' has a low priority."
    case _:
        reminder = f"Your task '{task}' has an unknown priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Output the customized reminder
print(reminder)
