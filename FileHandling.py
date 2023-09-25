import os 

def main():
    # It opens a file named "test.txt" in write mode ("w")
    # If the file doesn't exist, it will be created.
    # If it does exist, its contents will be truncated (erased)
    file = open ("test.txt", "w")
    # This writes the string "Hello World" to the "test.txt" file.
    file.write (" Hello World! ")
    # After writing to the file, it is important to close it to ensure that all changes are saved and resources are released.
    file.close()

    # This line opens the "test.txt" file in read mode ("r")
    # The file object is assigned to the variable f.
    with open ("test.txt", "r") as f:
        # Reads the contents of the file f and stores them in the variable text.
        text = f.read()
        print (text)
    
    lines=["Python is nice, ","Let's code more\n"]
    with open ("test.txt","a+") as f:
        # Writes the contents of the lines list to the end of the file f. 
        f.writelines(lines)
    
    # Reopens the "test.txt" file in read mode.
    with open ("test.txt","r") as f:
        # Prints the entire contents of the file, including the original "Hello World" and the appended lines.
        print(f.read())
        # Moves the file cursor (pointer) back to the beginning of the file.
        f.seek(0)
        # Reads and prints the first line of the file, which is "Hello World."
        print(f.readline())
    
    os.remove("test.txt")
    # os.remove("C:\\Sara's Documents\\Opikoodi Course\\Python\\test.txt")

if __name__ == "__main__":
    main()