Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> python
... # Get user input
... num1 = float(input("Enter the first number: "))
... num2 = float(input("Enter the second number: "))
... operation = input("Enter the operation (+, -, *, /): ")
... 
... # Perform the calculation based on the operation
... if operation == '+':
...     result = num1 + num2
... elif operation == '-':
...     result = num1 - num2
... elif operation == '*':
...     result = num1 * num2
... elif operation == '/':
...     if num2 == 0:
...         result = "Error! Division by zero is not allowed."
...     else:
...         result = num1 / num2
... else:
...     result = "Invalid operation entered."
... 
... # Print the result
