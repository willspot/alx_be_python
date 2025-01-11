from datetime import datetime, timedelta

# Funct to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time to "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Function to calculate the future date based on user input
def calculate_future_date():
    # Ask the user to input number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=number_of_days)
    # Print the future date in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main function to demonstrate the functionalities
def main():
    display_current_datetime()  # Display current date and time
    calculate_future_date()  # Calculate and display future date

if __name__ == "__main__":
    main()
