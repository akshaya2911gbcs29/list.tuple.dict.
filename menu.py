lst=list(map(int,input("Enter your list:").split()))
while True:
    print("1.Maximum")
    print("2.Minimum")
    print("3.slice")
    print("4.count")
    print("5.first occurrence")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Maximum:",max(lst))
    elif choice==2:
        print("Minimum:",min(lst))
    elif choice==3:
        print("Slice:",lst[1:4])
    elif choice==4:
        item=int(input("Enter num:"))
        print("Count:",lst.count(item))
    elif choice==5:
        item=int(input("Enter num:"))
        print("First Occurrence:",lst.index(item))
    elif choice==6:
        break
    else:
        print("Invalid Choice")
