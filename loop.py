# Outer loop runs from 0 to 5
for num in range(6):
    # Inner loop runs from 0 to num (num is included)
    for i in range(num):
        # Print the current 'num' in row, with a space at the end
        print(num, end=" ")
    # When inner loop finishes, print a newline to start a new line
    print("\n")