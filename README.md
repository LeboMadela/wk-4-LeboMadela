# wk-4-LeboMadela
Week 4 Python Assignment

## File Read, Write & Error Handling Program
## Overview
This Python program demonstrates how to:
- Read the contents of a file.
- Modify the contents.
- Write the modified content to a new file.
- Handle errors such as file not found, permission issues, and other unexpected errors.
The program contains two key functionalities:
- File Read & Write: Reads an input file, modifies its content, and writes the modified content to a new output file.
- Error Handling: Prompts the user for a filename and handles any errors that might occur during file reading, such as a file not being found or permission issues.

## Features
- Read file content and modify it (e.g., convert text to uppercase).
- Handle common file errors such as:
  - File not found
  - Permission denied
  - Other unforeseen errors

## Requirements
- Python 3.x or above
- A text editor to modify input and output files (e.g., Notepad, VS Code, etc.)

## How to Use
- File Read, Modify & Write:
  The program will read a file (e.g., input.txt), modify its content (for example, convert all text to uppercase), and write the modified content to a new file (e.g., output.txt).
- Error Handling:
  The program will prompt you to enter the name of a file. It will then attempt to read and display the content of the file. If the file cannot be read (due to not being found, permission issues, or other errors), the program will gracefully handle the error and provide a helpful message.

## Program Structure
1. read_and_write_file(input_filename, output_filename)
- Description: This function reads the content from the input file, modifies it, and writes the modified content to the output file.
- Parameters:
  - input_filename: The name of the file to read from.
  - output_filename: The name of the file to write the modified content to.
- Process:
  - Read the file content.
  - Modify the content (uppercase conversion is the default).
  - Write the modified content to a new file.

2. read_file_with_error_handling()
- Description: This function prompts the user to input a filename and attempts to read it. It handles errors gracefully if the file doesn't exist or if there are permission issues.
- Process:
  - Ask for the filename from the user.
  - Attempt to open the file and read the content.
  - Handle possible errors such as FileNotFoundError and PermissionError.
 
## Example Usage
# Example usage of the file read, modify, and write functionality
input_filename = 'input.txt'  # Replace with the actual input file you want to read from
output_filename = 'output.txt'  # Replace with the desired output file name
read_and_write_file(input_filename, output_filename)

# Example usage of the error handling functionality
read_file_with_error_handling()

## Error Handling
- FileNotFoundError: Raised when the specified file is not found.
- PermissionError: Raised when there is no permission to read the specified file.
- General Exception: Catches any other errors that occur unexpectedly.

## Notes
- Ensure that the input file exists and has the appropriate permissions before running the program.
- Modify the content processing step (e.g., upper()) to fit your needs (e.g., text transformation, data processing, etc.).

##License
This program is open-source and free to use. You can modify it as needed for personal or professional projects.
