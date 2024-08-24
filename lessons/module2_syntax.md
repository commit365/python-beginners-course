# Module 2: Basic Syntax and Data Types

## Topics Covered

- **Python Syntax and Indentation**
  - Understanding the importance of syntax in Python.
  - The role of indentation in defining code blocks.
  - Basic structure of a Python script.

- **Data Types**
  - **Integers**: Whole numbers (e.g., `1`, `42`, `-5`).
  - **Floats**: Decimal numbers (e.g., `3.14`, `-0.001`, `2.0`).
  - **Strings**: Text data enclosed in quotes (e.g., `"Hello"`, `'World'`).
  - **Booleans**: Logical values representing `True` or `False`.

- **Type Conversion and Basic Operations**
  - Converting between data types (e.g., `int` to `float`, `str` to `int`).
  - Basic arithmetic operations: addition, subtraction, multiplication, and division.
  - String operations: concatenation and repetition.

## Learning Outcomes

By the end of this module, learners will be able to:

- Write basic Python scripts using correct syntax and indentation.
- Manipulate different data types and perform basic operations on them.

## Activities

### 1. Exercises on Data Types and Operations

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `data_types_exercises.py`).

2. **Exercise 1: Working with Integers and Floats**
   - Write a script that performs the following operations:
     ```python
     # Declare variables
     a = 10
     b = 3.5

     # Perform arithmetic operations
     addition = a + b
     subtraction = a - b
     multiplication = a * b
     division = a / b

     # Print the results
     print("Addition:", addition)
     print("Subtraction:", subtraction)
     print("Multiplication:", multiplication)
     print("Division:", division)
     ```

3. **Exercise 2: Working with Strings**
   - Write a script that demonstrates string manipulation:
     ```python
     # Declare string variables
     first_name = "John"
     last_name = "Doe"

     # Concatenate strings
     full_name = first_name + " " + last_name

     # Print the full name
     print("Full Name:", full_name)

     # Repeat a string
     greeting = "Hello! " * 3
     print(greeting)
     ```

4. **Exercise 3: Type Conversion**
   - Write a script that converts between data types:
     ```python
     # Convert string to integer
     num_str = "42"
     num_int = int(num_str)

     # Convert integer to float
     num_float = float(num_int)

     # Print the converted values
     print("String to Integer:", num_int)
     print("Integer to Float:", num_float)
     ```

### 2. Quiz on Basic Syntax

**Instructions:**

1. **Create a New Quiz File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `syntax_quiz.py`).

2. **Quiz Questions:**
   - Write a script that asks the following questions and checks the answers:
     ```python
     # Quiz questions
     question1 = input("1. What is the correct way to start a Python comment?\n(a) //\n(b) #\n(c) /*\nYour answer: ")
     question2 = input("2. Which of the following is NOT a valid variable name?\n(a) my_var\n(b) 2ndVar\n(c) var2\nYour answer: ")
     question3 = input("3. What symbol is used for string concatenation?\n(a) +\n(b) &\n(c) *\nYour answer: ")

     # Check answers
     if question1.lower() == 'b':
         print("Correct! Comments in Python start with #.")
     else:
         print("Incorrect. The correct answer is (b) #.")

     if question2.lower() == 'b':
         print("Correct! Variable names cannot start with a number.")
     else:
         print("Incorrect. The correct answer is (b) 2ndVar.")

     if question3.lower() == 'a':
         print("Correct! The + symbol is used for string concatenation.")
     else:
         print("Incorrect. The correct answer is (a) +.")
     ```

## Conclusion

In this module, you have learned about Python syntax, data types, and basic operations. You practiced writing scripts that manipulate different data types and performed various operations. You are now ready to move on to the next module, where you will explore control flow in Python.