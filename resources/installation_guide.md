# Installation Guide for Python and Development Environment

This document provides a step-by-step guide to installing Python and setting up your development environment. Follow the instructions below to get started with Python programming.

## Step 1: Install Python

### Windows

1. **Download Python Installer**:
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Click on the "Download Python" button for the latest version.

2. **Run the Installer**:
   - Open the downloaded installer.
   - **Important**: Check the box that says "Add Python to PATH".
   - Click on "Install Now".

3. **Verify Installation**:
   - Open Command Prompt (search for `cmd` in the Start menu).
   - Type the following command and press Enter:
     ```bash
     python --version
     ```
   - You should see the installed Python version.

### macOS

1. **Download Python Installer**:
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Click on the "Download Python" button for the latest version.

2. **Run the Installer**:
   - Open the downloaded `.pkg` file.
   - Follow the prompts to install Python.

3. **Verify Installation**:
   - Open Terminal (you can find it in Applications > Utilities).
   - Type the following command and press Enter:
     ```bash
     python3 --version
     ```
   - You should see the installed Python version.

### Linux

1. **Update Package List**:
   - Open Terminal.
   - Run the following command to update your package list:
     ```bash
     sudo apt update
     ```

2. **Install Python**:
   - Run the following command to install Python:
     ```bash
     sudo apt install python3
     ```

3. **Verify Installation**:
   - Type the following command and press Enter:
     ```bash
     python3 --version
     ```
   - You should see the installed Python version.

## Step 2: Install pip

`pip` is the package installer for Python, allowing you to install additional libraries and packages.

### Windows and macOS

- `pip` is included automatically with Python installations from version 3.4 and above. You can verify its installation by running:
  ```bash
  pip --version
  ```

### Linux

- If `pip` is not installed, you can install it using:
  ```bash
  sudo apt install python3-pip
  ```

## Step 3: Install a Code Editor or IDE

You can choose from several code editors or Integrated Development Environments (IDEs) to write your Python code. Here are some popular options:

### Visual Studio Code (VSCode)

1. **Download VSCode**:
   - Go to the [Visual Studio Code website](https://code.visualstudio.com/).
   - Click on the "Download" button for your operating system.

2. **Install VSCode**:
   - Run the downloaded installer and follow the prompts.

3. **Install Python Extension**:
   - Open VSCode.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
   - Search for "Python" and install the official Python extension by Microsoft.

### PyCharm

1. **Download PyCharm**:
   - Go to the [JetBrains PyCharm website](https://www.jetbrains.com/pycharm/download/).
   - Download the Community Edition (free).

2. **Install PyCharm**:
   - Run the downloaded installer and follow the prompts.

### Jupyter Notebook

Jupyter Notebook is an interactive environment that allows you to write and execute Python code in a web browser.

1. **Install Jupyter Notebook**:
   - Open your command line interface (Command Prompt, Terminal).
   - Run the following command:
     ```bash
     pip install notebook
     ```

2. **Launch Jupyter Notebook**:
   - In your command line interface, navigate to your desired directory and run:
     ```bash
     jupyter notebook
     ```
   - This will open Jupyter in your web browser.

## Conclusion

You have successfully installed Python, `pip`, and set up your development environment. You are now ready to start coding in Python! If you encounter any issues during installation, please refer to the official documentation or seek help from the community.