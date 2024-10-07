import difflib
import sys
import re

# Function to insert line breaks after specific characters
def insert_line_breaks(text):
    for char in [';', '}', '{']:
        text = text.replace(char, char + '\n')
    return text

def remove_comments(text):
    # Remove single-line comments
    text = re.sub(r'//.*', '', text)
    # Remove multi-line comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text

def remove_all_whitespace(text):
    """Remove all whitespace from a string."""
    # Remove all whitespace (spaces, tabs, line breaks, etc.)
    return ''.join(text.split())


def read_and_format(file_path):
    """Read a file, format it by inserting line breaks, and normalize spaces."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # First, insert line breaks after specific characters
        content_no_comments = remove_comments(content)
        formatted_content = remove_all_whitespace(content_no_comments)
        formatted_content = insert_line_breaks(formatted_content)
        return formatted_content

def compare_files(file1_path, file2_path):
    # Read and format files
    file1_content = read_and_format(file1_path)
    file2_content = read_and_format(file2_path)

    # Use difflib to find differences and generate a diff for formatted representations
    diff = difflib.unified_diff(
        file1_content.splitlines(keepends=True), 
        file2_content.splitlines(keepends=True),
        fromfile=file1_path,
        tofile=file2_path,
        lineterm=''
    )
    in_diff_block = False
    outputContent = ''
    for line in diff:
        outputContent += line
    #save as output.txt
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(outputContent)


# Example usage (compare  files, one from folder Local and one from folder ShareDrive)
compare_files('local/.HTML', 'shareDrive/.HTML')