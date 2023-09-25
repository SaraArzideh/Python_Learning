def If_divisible(list):
    print(f"Given list is: {list} and It's devisible by 5 numbers are: ")
    for num in list:
        if num % 5==0:
            print(num)

list1=[10, 20, 33, 46, 55]
If_divisible(list1)

list2=[1002, 200,430,86,9]
If_divisible(list2)
    