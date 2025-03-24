# Function to perform the operation based on user input
def perform_operation(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Ensure we don't divide by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Error: Invalid operation. Please enter +, -, *, or /."
    
    return f"{num1} {operation} {num2} = {result}"

# Main program to get user input and display the result
def main():
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation and print the result
    result = perform_operation(num1, num2, operation)
    print(result)

# Run the main program
if __name__ == "__main__":
    main()
    