0. Weather Recommendation Program
Utilize conditional statements to guide program execution based on user input regarding weather conditions.

Create a Python script named weather_advice.py. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

Instructions:

Prompt User for Weather Input:

Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
Use the prompt: What's the weather like today? (sunny/rainy/cold):.
Provide Clothing Recommendations:

Based on the user’s input, your program will recommend different types of clothing:
If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.
Output the Recommendation:

Print the clothing recommendation based on the weather condition provided by the user.

1. Simple Calculator with Match Case
Learn to use Match Case statements for handling multiple operations in a simple calculator program.

Task Description:

Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

Instructions:

Prompt for User Input:

Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
Make sure you use num1 and num2 for first and second numbers
Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.
Perform the Calculation Using Match Case:

Implement a Match Case statement that executes the chosen operation based on the user’s input.
For addition (+), subtract (-), multiply (*), and divide (/).
Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.
Output the Result:

Display the result of the operation in a user-friendly message, e.g., The result is [result].

2. Multiplication Table Generator
Use a for loop to generate and print the multiplication table for a given number.

Task Description:

Create a Python script named multiplication_table.py. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

Instructions:

Prompt User for a Number:

Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
Save it in a variable name number
Generate and Print the Multiplication Table:

Use a for loop to iterate through the numbers 1 to 10.
For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.

3. Drawing Patterns with Nested Loops
Utilize while loops and nested for loops to draw a simple text-based pattern.

Task Description:

Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

Instructions:

Prompt User for Pattern Size:

Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
Draw the Pattern:

First, use a while loop to iterate through each row of the pattern.
Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
After completing each row, print a newline character to move to the next row.
Continue until the pattern forms a square of the inputted size.

4. Personal Daily Reminder
Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

Task Description:

Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
Provide a Customized Reminder:

Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
A message should be ‘that requires immediate attention today!’


