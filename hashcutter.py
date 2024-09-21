def remove_all_spaces(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the file contents
            content = file.read()
            
            # Remove all spaces (including newlines and tabs)
            cleaned_content = content.replace('\n', '').replace('\r', '').replace(' ', '').replace('\t', '')

        return cleaned_content

    except FileNotFoundError:
        return "Error: The file was not found."

# Ask the user for the file path
user_file_path = input("Please provide the path to your file: ")

# Perform the operation and print the result
cleaned_text = remove_all_spaces(user_file_path)
print(cleaned_text)
