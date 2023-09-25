# Read input text from a file
"""
file_path = input("Enter the path to the file containing the text: ")

try:
    with open(file_path, 'r') as file:
        string = file.read()
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    exit()
"""
string=input("Which text do you like to work on?")
substring= input("which substring do you like to count in above text?")

def count_substring(string, substring):
    print("Given string is: ", string)
    count=0
    for i in range(len(string)):
        count+= string[i:i+len(substring)]==substring
    return count
count= count_substring(string, substring)
print(f"{substring} appeared {count} times in the given text")
