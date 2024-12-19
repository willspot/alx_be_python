task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

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
    reminder += " That requires immediate attention today!"

# Output the customized reminder
print(reminder)
