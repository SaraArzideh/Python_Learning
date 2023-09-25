def Check_Palindrome():
    given_num=int(input(("enter a numer to check palindrome!")))
    print(f"Given number is {given_num}")

    # Reverse the given number
    """
    #first way:
    reverse_num=0
    remainder=0
    A=len("{given_num}")
    for i in range(1,A):
        remainder=(given_num -remainder) % (10**i)
        reverse_num= remainder * (10 **(A-((2*i)-1)))+reverse_num
    print(f"reverse number is: {reverse_num}")
    """
    #second way:
    given_num_str= str(given_num) #integer to string
    reversed_str=given_num_str[::-1]
    reverse_num=int(reversed_str)
    print(f"reverse number is: {reverse_num}")

    # Check the numbers
    if given_num==reverse_num:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")

if __name__=="__main__":
    Check_Palindrome()

