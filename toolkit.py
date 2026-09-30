"""A small interactive toolkit with a calculator, to-do list, and number checker."""


# Tool 1: Simple Calculator
# This tool performs basic calculations using two numbers.
def simple_calculator():
	print("\n--- Simple Calculator ---")

	try:
		number1 = float(input("Enter the first number: "))
		number2 = float(input("Enter the second number: "))

		print("\nChoose an operation:")
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")

		operation = input("Enter your choice: ")

		if operation == "1":
			result = number1 + number2
			print(f"Result: {number1} + {number2} = {result}")
		elif operation == "2":
			result = number1 - number2
			print(f"Result: {number1} - {number2} = {result}")
		elif operation == "3":
			result = number1 * number2
			print(f"Result: {number1} × {number2} = {result}")
		elif operation == "4":
			if number2 == 0:
				print("Sorry, you cannot divide by zero.")
			else:
				result = number1 / number2
				print(f"Result: {number1} ÷ {number2} = {result}")
		else:
			print(f"Sorry, {operation} is not a valid operation.")

	except ValueError:
		print("Please enter valid numbers.")


# Tool 2: To-Do List
# This tool lets the user add, view, and remove tasks from a changing list.
def todo_list():
	tasks = []

	print("\n--- To-Do List ---")

	while True:
		print("\nTo-Do List Options:")
		print("1. Add a task")
		print("2. View tasks")
		print("3. Remove a task")
		print("4. Return to main menu")

		choice = input("Enter your choice: ")

		if choice == "1":
			task = input("Enter a task: ")
			tasks.append(task)
			print(f"Task added: {task}")
		elif choice == "2":
			if not tasks:
				print("Your to-do list is empty.")
			else:
				print("\nYour tasks:")
				for number, task in enumerate(tasks, start=1):
					print(f"{number}. {task}")
		elif choice == "3":
			if not tasks:
				print("There are no tasks to remove.")
			else:
				for number, task in enumerate(tasks, start=1):
					print(f"{number}. {task}")

				try:
					task_number = int(input("Enter the task number to remove: "))
					if 1 <= task_number <= len(tasks):
						removed_task = tasks.pop(task_number - 1)
						print(f"Removed task: {removed_task}")
					else:
						print("That task number does not exist.")
				except ValueError:
					print("Please enter a valid task number.")
		elif choice == "4":
			print("Returning to the main menu...")
			break
		else:
			print("Sorry, that is not a valid option.")


# Tool 3: Number Checker
# This tool checks whether a number is positive, negative, or zero.
def number_checker():
	print("\n--- Number Checker ---")

	try:
		number = float(input("Enter a number: "))
		if number > 0:
			print(f"{number} is a positive number.")
		elif number < 0:
			print(f"{number} is a negative number.")
		else:
			print(f"{number} is zero.")
	except ValueError:
		print("Please enter a valid number.")


# Main menu
# This loop keeps the toolkit running until the user chooses Quit.
def main():
	print("====================================")
	print("Welcome to My Python Toolkit!")
	print("====================================")

	while True:
		print("\nPlease choose a tool:")
		print("1. Simple Calculator")
		print("2. To-Do List")
		print("3. Number Checker")
		print("4. Quit")

		choice = input("Enter your choice: ")
		if choice == "1":
			simple_calculator()
		elif choice == "2":
			todo_list()
		elif choice == "3":
			number_checker()
		elif choice == "4":
			print("\nThank you for using My Python Toolkit!")
			print("Goodbye!")
			break
		else:
			print(f"Sorry, '{choice}' is not on the menu. Please choose 1, 2, 3, or 4.")


# Start the program
if __name__ == "__main__":
	main()
