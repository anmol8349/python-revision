l1=[]

while True:
    print("\n ---- menu-----")
    print("\n1.add")
    print("\n2.remove")
    print("\n3.display")
    print("\n4.search")
    print("\n5.exit")
    
    choice=int(input("enter choice  "))
    
    # add
    if choice ==1:
        item = input("enter elt to append")
        l1.append(item)
        print("added succesfully")
        
    elif choice==2:
        item = input("enter element to remove")
        
        if item in l1:
            l1.remove(item)
            print("removed")
        else:
            print("not removed")
            
    elif choice==3:
        if len(l1)==0:
            print("list is empty")
        else:
          print(l1)
          
    elif choice==4:
        item = input("enter elt to search")
        
        if item in l1:
            print("found")
        else:
            print("not found")
            
    elif choice==5:
        break
    
    else:
        print("enter valid")