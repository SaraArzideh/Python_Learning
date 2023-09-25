# Calculate income tax
income=int(input("enter the income"))
def tax(income):
    # First 10000: 0
    if income <=10000:
        Tax=0
    # Second 10000: 10%
    elif income <20000:
        Tax=((income-10000)*0.10)
    # Over 10000: second 10000:10% and remaining:20%
    else:
        Tax=(10000)*0.10+((income-20000)*0.20)
    return Tax
print(f"The given income tax is {tax(income)} dollars.")

if __name__=="__main__":
    tax(income)