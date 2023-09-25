base=int(input("enter a number as a base"))
exp=int(input("enter a number as a power"))

def exponent(base, exp):
    result=1
    for i in range(exp):
        result=result*base
    return result
print(f"{base}^{exp} = {exponent(base,exp)}")

if __name__=="__main__":
    exponent(base,exp) 