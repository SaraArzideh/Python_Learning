# Create a conditional combined list
def comb_list(list1, list2):
    Comb_list=[]
    # Iterate first list
    for num in list1:
        if num%2!=0:
            Comb_list.append(num)
    # Iterate second list
    for num in list2:
        if num%2==0:
            Comb_list.append(num)
    print (f"combinated list is {Comb_list}")

Set1=[25,10,12,36,43,90]
Set2=[1003,1008,1047,1050,1089,1096]
 
if __name__=="__main__":
    comb_list(Set1, Set2)