# Module 6: File Handling

## Topics Covered

- **Reading from and Writing to Files**
  - Understanding how to open, read, and write data to files in Python.
  - Using the `open()` function to manage file operations.

- **File Modes and Exception Handling**
  - Exploring different file modes: read (`'r'`), write (`'w'`), append (`'a'`), and read/write (`'r+'`).
  - Implementing exception handling using `try`, `except`, and `finally` to manage errors during file operations.

- **Working with File Paths**
  - Understanding absolute and relative file paths.
  - Using the `os` module to manipulate file paths.

## Learning Outcomes

By the end of this module, learners will be able to:

- Manage files in Python, including reading from and writing to files.
- Handle errors and exceptions gracefully during file operations.

## Activities

### 1. Exercises on File Operations

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `file_handling_exercises.py`).

2. **Exercise 1: Writing to a File**
   - Write a script that creates a new text file and writes some text to it:
     ```python
     # Writing to a file
     with open('example.txt', 'w') as file:
         file.write("Hello, World!\n")
         file.write("This is a file handling exercise.\n")
     print("Data written to example.txt")
     ```

3. **Exercise 2: Reading from a File**
   - Write a script that reads the contents of the file you created in Exercise 1:
     ```python
     # Reading from a file
     with open('example.txt', 'r') as file:
         content = file.read()
         print("File contents:")
         print(content)
     ```

4. **Exercise 3: Appending to a File**
   - Write a script that appends more text to the existing file:
     ```python
     # Appending to a file
     with open('example.txt', 'a') as file:
         file.write("Appending a new line to the file.\n")
     print("Data appended to example.txt")
     ```

5. **Exercise 4: Exception Handling**
   - Write a script that attempts to read a file that may not exist and handles the exception:
     ```python
     # Exception handling
     try:
         with open('non_existent_file.txt', 'r') as file:
             content = file.read()
     except FileNotFoundError:
         print("Error: The file does not exist.")
     finally:
         print("Finished attempting to read the file.")
     ```

### 2. Project: Create a Text-Based Contact Book

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `contact_book.py`).

2. **Contact Book Logic:**
   - Write a script that allows users to add, view, and search for contacts:
     ```python
     import os

     # Define the contact book file
     contact_file = 'contacts.txt'

     def add_contact(name, phone):
         with open(contact_file, 'a') as file:
             file.write(f"{name},{phone}\n")
         print(f"Contact {name} added.")

     def view_contacts():
         if os.path.exists(contact_file):
             with open(contact_file, 'r') as file:
                 print("Contacts:")
                 for line in file:
                     name, phone = line.strip().split(',')
                     print(f"Name: {name}, Phone: {phone}")
         else:
             print("No contacts found.")

     def search_contact(name):
         if os.path.exists(contact_file):
             with open(contact_file, 'r') as file:
                 for line in file:
                     contact_name, phone = line.strip().split(',')
                     if contact_name.lower() == name.lower():
                         print(f"Found: Name: {contact_name}, Phone: {phone}")
                         return
         print("Contact not found.")

     # Main program loop
     while True:
         print("\nContact Book")
         print("1. Add Contact")
         print("2. View Contacts")
         print("3. Search Contact")
         print("4. Exit")
         choice = input("Choose an option: ")

         if choice == '1':
             name = input("Enter contact name: ")
             phone = input("Enter contact phone: ")
             add_contact(name, phone)
         elif choice == '2':
             view_contacts()
         elif choice == '3':
             name = input("Enter the name to search: ")
             search_contact(name)
         elif choice == '4':
             print("Exiting the contact book.")
             break
         else:
             print("Invalid choice. Please try again.")
     ```

## Conclusion

In this module, you learned about file handling in Python, including how to read from and write to files, manage file modes, and handle exceptions. You practiced file operations through hands-on exercises and created a text-based contact book project to apply your skills. You are now ready to move on to the next module, where you will explore libraries in Python. Happy coding!