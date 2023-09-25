k=6
for i in range(1,6):
    for j in range(1,k):
        print("*" , end="   ")  # k times writes * in a row
    print("\n")                 # When inner loop finishes, prints a new line
    k=k-1