# analysis.py

import pandas as pd
from sklearn.datasets import load_iris

def load_data():
    """Load the Iris dataset."""
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['species'] = iris.target
    data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    return data

def basic_analysis(data):
    """Perform basic analysis on the dataset."""
    print("First 5 rows of the dataset:")
    print(data.head())

    print("\nBasic Statistics:")
    print(data.describe())

    print("\nSpecies Count:")
    print(data['species'].value_counts())

    print("\nAverage Sepal Length by Species:")
    average_sepal_length = data.groupby('species')['sepal length (cm)'].mean()
    print(average_sepal_length)

def main():
    """Main function to run the analysis."""
    data = load_data()
    basic_analysis(data)

if __name__ == "__main__":
    main()
