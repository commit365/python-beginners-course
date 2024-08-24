# Module 3: Control Flow

## Topics Covered

- **Conditional Statements**
  - Understanding how to use `if`, `elif`, and `else` to make decisions in your code.
  - Syntax and examples of conditional statements.

- **Loops**
  - **For Loops**: Iterating over a sequence (e.g., lists, strings).
  - **While Loops**: Repeating a block of code as long as a condition is true.

- **Loop Control Statements**
  - **Break**: Exiting a loop prematurely.
  - **Continue**: Skipping the current iteration and continuing with the next one.

## Learning Outcomes

By the end of this module, learners will be able to:

- Implement decision-making in Python code using conditional statements.
- Use loops to iterate over data and perform repetitive tasks.

## Activities

### 1. Coding Exercises on Control Flow

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `control_flow_exercises.py`).

2. **Exercise 1: Conditional Statements**
   - Write a script that checks a user's age and prints whether they are a minor, adult, or senior:
     ```python
     # Get user input
     age = int(input("Enter your age: "))

     # Conditional statements
     if age < 18:
         print("You are a minor.")
     elif 18 <= age < 65:
         print("You are an adult.")
     else:
         print("You are a senior.")
     ```

3. **Exercise 2: For Loop**
   - Write a script that prints the squares of numbers from 1 to 10:
     ```python
     # For loop to print squares
     for i in range(1, 11):
         square = i ** 2
         print(f"The square of {i} is {square}.")
     ```

4. **Exercise 3: While Loop**
   - Write a script that prompts the user to enter a password until they enter the correct one:
     ```python
     # Password check using while loop
     correct_password = "python123"
     user_password = ""

     while user_password != correct_password:
         user_password = input("Enter the password: ")
         if user_password != correct_password:
             print("Incorrect password. Try again.")
     print("Access granted!")
     ```

5. **Exercise 4: Loop Control Statements**
   - Write a script that prints numbers from 1 to 10, but skips the number 5:
     ```python
     # Using continue statement
     for i in range(1, 11):
         if i == 5:
             continue
         print(i)
     ```

### 2. Mini-Project: Create a Simple Number Guessing Game

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `number_guessing_game.py`).

2. **Game Logic:**
   - Write a script that generates a random number and prompts the user to guess it:
     ```python
     import random

     # Generate a random number between 1 and 100
     secret_number = random.randint(1, 100)
     guess = None
     attempts = 0

     print("Welcome to the Number Guessing Game!")
     print("I have selected a number between 1 and 100. Can you guess it?")

     # Loop until the user guesses the correct number
     while guess != secret_number:
         guess = int(input("Enter your guess: "))
         attempts += 1

         if guess < secret_number:
             print("Too low! Try again.")
         elif guess > secret_number:
             print("Too high! Try again.")
         else:
             print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
     ```

## Conclusion

In this module, you learned about control flow in Python, including conditional statements and loops. You practiced implementing decision-making and iterating over data. You also created a mini-project, a number guessing game, to apply your skills in a fun and interactive way. You are now ready to move on to the next module, where you will explore functions and modules in Python. 