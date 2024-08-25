# Module 7: Introduction to Libraries

## Topics Covered

- **Installing and Importing Libraries Using `pip`**
  - Understanding how to use `pip` to install external libraries.
  - Importing libraries into your Python scripts.

- **Overview of NumPy and Pandas**
  - Introduction to NumPy: a library for numerical operations and array manipulation.
  - Introduction to Pandas: a library for data manipulation and analysis using DataFrames.

- **Basic Data Manipulation with Libraries**
  - Performing basic operations with NumPy arrays and Pandas DataFrames.
  - Understanding how to read and write data using Pandas.

## Learning Outcomes

By the end of this module, learners will be able to:

- Leverage external libraries for enhanced functionality in Python.
- Perform basic data analysis using NumPy and Pandas.

## Activities

### 1. Exercises Using NumPy and Pandas

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `libraries_exercises.py`).

2. **Exercise 1: Installing Libraries**
   - Install NumPy and Pandas using `pip` in your command line:
     ```bash
     pip install numpy pandas
     ```

3. **Exercise 2: Using NumPy**
   - Write a script that demonstrates basic NumPy operations:
     ```python
     import numpy as np

     # Create a NumPy array
     array = np.array([1, 2, 3, 4, 5])

     # Perform basic operations
     array_squared = array ** 2
     array_sum = np.sum(array)

     # Print results
     print("Original Array:", array)
     print("Squared Array:", array_squared)
     print("Sum of Array:", array_sum)
     ```

4. **Exercise 3: Using Pandas**
   - Write a script that creates a simple DataFrame and performs basic operations:
     ```python
     import pandas as pd

     # Create a DataFrame
     data = {
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'City': ['New York', 'Los Angeles', 'Chicago']
     }
     df = pd.DataFrame(data)

     # Display the DataFrame
     print("DataFrame:\n", df)

     # Access a column
     print("Names:", df['Name'])

     # Calculate the average age
     average_age = df['Age'].mean()
     print("Average Age:", average_age)
     ```

### 2. Mini-Project: Analyze a Dataset Using Pandas

**Instructions:**

1. **Create a New Python File:**
   - Open your IDE or Jupyter Notebook and create a new Python file (e.g., `data_analysis.py`).

2. **Download a Sample Dataset:**
   - For this project, you can use a sample dataset, such as the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris), or any CSV file you have.

3. **Data Analysis Logic:**
   - Write a script that reads the dataset and performs some basic analysis:
     ```python
     import pandas as pd

     # Load the dataset (replace 'iris.csv' with your dataset file)
     df = pd.read_csv('iris.csv')

     # Display the first few rows of the DataFrame
     print("First 5 rows of the dataset:\n", df.head())

     # Display basic statistics
     print("\nBasic Statistics:\n", df.describe())

     # Count the number of occurrences of each species
     species_count = df['species'].value_counts()
     print("\nSpecies Count:\n", species_count)

     # Calculate the average sepal length
     average_sepal_length = df['sepal_length'].mean()
     print("Average Sepal Length:", average_sepal_length)
     ```

## Conclusion

In this module, you learned about the importance of libraries in Python and how to install and import them using `pip`. You explored NumPy and Pandas, performing basic data manipulation and analysis. Through hands-on exercises and a mini-project, you gained practical experience using these powerful libraries. You are now ready to move on to the next module, where you will explore capstone projects in Python.