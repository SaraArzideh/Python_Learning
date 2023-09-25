Word=input("enter a word")
i=int(input("How many first characters do you wish to remove from the given word?"))

if i <= len(Word):
    print (f"This is the result after removing first {i} characterst: {(Word[i:])}")
else:
    i2=int(input("Your number should be less than the word's length!, enter another number"))
    if i2 <= len(Word):
        print (f"This is the result after removing first {i2} characterst: {(Word[i2:])}")

