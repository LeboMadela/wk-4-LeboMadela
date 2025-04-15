#Author: Moleboheng Madela
#Date: 2025-04-15
# This program reads a file, modifies its content, and writes the modified content to a new file.
# It also includes error handling in case the file can't be found or read.

# Function to read, modify, and write content to a new file
def read_and_write_file(input_filename, output_filename):
    try:
        # Step 1: Open the input file in 'read' mode ('r')
        # This allows us to read the content of the file.
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the entire content of the file

        # Step 2: Modify the content of the file
        # For example, here we convert the content to uppercase.
        modified_content = content.upper()  # Modify as needed (could be any modification)

        # Step 3: Open the output file in 'write' mode ('w')
        # This allows us to write the modified content to the new file.
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)  # Write the modified content to the output file

        # Step 4: Notify the user that the process is complete
        print(f"Content from '{input_filename}' has been modified and written to '{output_filename}'.")

    except Exception as e:
        # If an error occurs, we catch the exception and print the error message
        print(f"Error: {e}")

# Function to handle user input and read a file with error handling
def read_file_with_error_handling():
    # Step 1: Ask the user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Attempt to open and read the file
        # The 'r' mode allows us to read the file
        with open(filename, 'r') as file:
            content = file.read()  # Read the content of the file
            print("File content successfully read:")
            print(content)  # Display the content of the file

    except FileNotFoundError:
        # This block handles the case where the file doesn't exist
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        # This block handles the case where the user doesn't have permission to read the file
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        # This block catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage:
# 1. We will call the function to read, modify, and write the file.
input_filename = 'input.txt'  # Replace with the actual input file you want to read from
output_filename = 'output.txt'  # Replace with the desired output file name
read_and_write_file(input_filename, output_filename)

# 2. We will call the function to handle file reading with error handling based on user input
read_file_with_error_handling()
