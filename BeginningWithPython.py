def product (num1,num2):
    if num1*num2 <= 1000:
        return num1*num2
    else:
        return num1+num2
    
num1= int(input("Enter first number"))
num2 = int(input("Enter second number"))

print (f"The result is {product(num1,num2)}")

if __name__ == "__main__":
    product(num1,num2)