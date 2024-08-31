# Module 4: Functions and Modules

## Topics Covered

- **Defining and Calling Functions**
  - Understanding the syntax for defining functions using the `def` keyword.
  - How to call functions and pass arguments.

- **Function Parameters and Return Values**
  - Using parameters to pass information to functions.
  - Returning values from functions using the `return` statement.

- **Importing and Using Modules**
  - How to import built-in modules and use their functions.
  - Creating and importing your own modules.

## Learning Outcomes

By the end of this module, learners will be able to:

- Write reusable code using functions.
- Utilize Python's standard library by importing and using modules.

## Activities

### 1. Exercises on Writing Functions

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `functions_exercises.py`).

2. **Exercise 1: Defining a Function**
   - Write a function that takes two numbers as parameters and returns their sum:
     ```python
     def add_numbers(num1, num2):
         return num1 + num2

     # Test the function
     result = add_numbers(5, 3)
     print("The sum is:", result)
     ```

3. **Exercise 2: Function with Default Parameter**
   - Write a function that greets a user with a default name:
     ```python
     def greet_user(name="Guest"):
         print(f"Hello, {name}!")

     # Test the function with and without an argument
     greet_user("Alice")
     greet_user()
     ```

4. **Exercise 3: Function with Return Value**
   - Write a function that calculates the area of a rectangle:
     ```python
     def calculate_area(length, width):
         return length * width

     # Test the function
     area = calculate_area(4, 5)
     print("The area of the rectangle is:", area)
     ```

5. **Exercise 4: Importing a Module**
   - Write a script that uses the `math` module to calculate the square root of a number:
     ```python
     import math

     number = 16
     square_root = math.sqrt(number)
     print(f"The square root of {number} is {square_root}.")
     ```

### 2. Project: Build a Calculator Using Functions

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `calculator.py`).

2. **Calculator Logic:**
   - Write a simple calculator that can perform addition, subtraction, multiplication, and division using functions:
     ```python
     def add(x, y):
         return x + y

     def subtract(x, y):
         return x - y

     def multiply(x, y):
         return x * y

     def divide(x, y):
         if y == 0:
             return "Cannot divide by zero!"
         return x / y

     print("Select operation:")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")

     choice = input("Enter choice (1/2/3/4): ")

     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))

     if choice == '1':
         print("Result:", add(num1, num2))
     elif choice == '2':
         print("Result:", subtract(num1, num2))
     elif choice == '3':
         print("Result:", multiply(num1, num2))
     elif choice == '4':
         print("Result:", divide(num1, num2))
     else:
         print("Invalid input!")
     ```

## Conclusion

In this module, you learned about functions and modules in Python, including how to define and call functions, use parameters and return values, and import modules. You practiced writing reusable code and built a simple calculator project to apply your skills. You are now ready to move on to the next module, where you will explore data structures in Python. 

Next: [5. Data Structures](./module5_data_structures.md)