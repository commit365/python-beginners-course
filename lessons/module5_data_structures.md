# Module 5: Data Structures

## Topics Covered

- **Lists, Tuples, Sets, and Dictionaries**
  - Understanding the characteristics and use cases of each data structure:
    - **Lists**: Ordered, mutable collections of items.
    - **Tuples**: Ordered, immutable collections of items.
    - **Sets**: Unordered collections of unique items.
    - **Dictionaries**: Unordered collections of key-value pairs.

- **Common Methods and Operations for Each Data Structure**
  - Methods for adding, removing, and accessing elements.
  - Iterating through data structures.

- **Nested Data Structures**
  - Understanding how to create and manipulate data structures that contain other data structures.

## Learning Outcomes

By the end of this module, learners will be able to:

- Use built-in data structures effectively in Python.
- Manipulate and access data within lists, tuples, sets, and dictionaries.

## Activities

### 1. Hands-On Exercises with Data Structures

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `data_structures_exercises.py`).

2. **Exercise 1: Working with Lists**
   - Create a list of your favorite fruits and perform the following operations:
     ```python
     # Create a list of fruits
     fruits = ["apple", "banana", "cherry", "date"]

     # Add a fruit to the list
     fruits.append("elderberry")

     # Remove a fruit from the list
     fruits.remove("banana")

     # Access the first fruit in the list
     first_fruit = fruits[0]

     # Print the results
     print("Fruits:", fruits)
     print("First fruit:", first_fruit)
     ```

3. **Exercise 2: Working with Tuples**
   - Create a tuple to store the coordinates of a point and demonstrate accessing its elements:
     ```python
     # Create a tuple of coordinates
     coordinates = (10, 20)

     # Access elements in the tuple
     x = coordinates[0]
     y = coordinates[1]

     # Print the coordinates
     print("Coordinates:", coordinates)
     print("X:", x)
     print("Y:", y)
     ```

4. **Exercise 3: Working with Sets**
   - Create a set of unique colors and demonstrate adding and removing colors:
     ```python
     # Create a set of colors
     colors = {"red", "green", "blue"}

     # Add a new color
     colors.add("yellow")

     # Remove a color
     colors.discard("green")

     # Print the results
     print("Colors:", colors)
     ```

5. **Exercise 4: Working with Dictionaries**
   - Create a dictionary to store information about a person and demonstrate accessing values:
     ```python
     # Create a dictionary
     person = {
         "name": "Alice",
         "age": 30,
         "city": "New York"
     }

     # Access values in the dictionary
     name = person["name"]
     age = person["age"]

     # Print the person's information
     print("Name:", name)
     print("Age:", age)
     ```

6. **Exercise 5: Nested Data Structures**
   - Create a list of dictionaries to store information about multiple people:
     ```python
     # Create a list of dictionaries
     people = [
         {"name": "Alice", "age": 30},
         {"name": "Bob", "age": 25},
         {"name": "Charlie", "age": 35}
     ]

     # Print each person's information
     for person in people:
         print(f"Name: {person['name']}, Age: {person['age']}")
     ```

### 2. Quiz on Data Structure Operations

**Instructions:**

1. **Create a New Quiz File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `data_structures_quiz.py`).

2. **Quiz Questions:**
   - Write a script that asks the following questions and checks the answers:
     ```python
     # Quiz questions
     question1 = input("1. Which data structure is ordered and mutable?\n(a) Set\n(b) List\n(c) Tuple\nYour answer: ")
     question2 = input("2. Which data structure cannot contain duplicate elements?\n(a) List\n(b) Dictionary\n(c) Set\nYour answer: ")
     question3 = input("3. How do you access the first element of a list named 'my_list'?\n(a) my_list[0]\n(b) my_list(0)\n(c) my_list.first()\nYour answer: ")

     # Check answers
     if question1.lower() == 'b':
         print("Correct! Lists are ordered and mutable.")
     else:
         print("Incorrect. The correct answer is (b) List.")

     if question2.lower() == 'c':
         print("Correct! Sets cannot contain duplicate elements.")
     else:
         print("Incorrect. The correct answer is (c) Set.")

     if question3.lower() == 'a':
         print("Correct! You access the first element of a list with my_list[0].")
     else:
         print("Incorrect. The correct answer is (a) my_list[0].")
     ```

## Conclusion

In this module, you learned about various data structures in Python, including lists, tuples, sets, and dictionaries. You practiced using these structures through hands-on exercises and completed a quiz to reinforce your understanding. You are now ready to move on to the next module, where you will explore file handling in Python. 

Next: [6. File Handling](./module6_file_handling.md)