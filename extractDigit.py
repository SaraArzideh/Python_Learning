# Extract digits from the end!
given_num=input(" Enter a number") #now given_num is a string
reversed_given_num= given_num[::-1]
for num in reversed_given_num:
    print(num, end=" ")