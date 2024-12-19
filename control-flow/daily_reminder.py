task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        reminder = f"reminder: '{task}' is a high priority."
    case "medium":
        reminder = f"reminder: '{task}' is a medium priority."
    case "low":
        reminder = f"reminder: '{task}' is a low priority."
    case _:
        reminder = f"reminder: '{task}' is an unknown priority."

if time_bound == "yes":
    reminder += " That requires immediate attention today!"

print(reminder)
