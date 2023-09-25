def main():
    # This is a List to store multiple items in a single variable
    mylist= ["apple","banana","orange"]
    print (mylist)

    mylist.append("lemon")
    print(mylist)
    mylist_copy= mylist.copy()
    mylist.extend(mylist_copy)
    print(mylist)
    myslice = mylist[3:]
    print(myslice)

    mytuple=("apple","banana","orange")
    print(mytuple)

    mydict={
        "brand":"Lenovo",
        "model": "Thinkpad",
        "screen": "15,4"
    }
    print(mydict)
    print(mydict["brand"])
    print(mydict["screen"])

    for key in mydict:
        print (key)
    for values in mydict.values():
        print(values)

    myset = {"apple","banana","orange",1,2,3}
    print(myset)
    myset.add(100)
    print(myset)
    

if __name__ == "__main__":
    main()