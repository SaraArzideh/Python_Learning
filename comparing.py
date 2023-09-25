def If_The_same(list):
    print(f"Given list is: {list}")
    num1=list[0]
    num2=list[-1]
    if num1 == num2:
        return True
    else:
        return False
list1=[10, 20, 30, 40, 10]
print(f"If the first and last characters are the same: {If_The_same(list1)}")

list2=[75, 65,35,75,30]
print(f"If the first and last characters are the same: {If_The_same(list2)}")
    