students =[]


def add_student():
    roll = int(input("enter roll no  :"))
    
    for s in students:
        if s["roll"]==roll:
            print("alredy exist")
            return
    name = input("enter name  ")
    marks = input("entyer marks :")
    
    student={
        "roll":roll,
        "name":name,
        "marks":marks
    }
    
    students.append(student)
    print("appended")
    
def display():
    if not students:
        print(" no record")
        return
    for s in students:
        print(f"roll= {s["roll"]} || name= {s["name"] } || marks= {s["marks"]} ")
        
        
def search():
    r=int(input("enter roll to serch"))
    
    for s in students:
        if s["roll"]==r:
            print("found")
    
    else:
        print("not found")
        
def remove():
    rr=int(input("enter roll to remove"))
    
    for s in students:
        if s["roll"]==r:
            students.remove(s)
            print("✅ Student deleted successfully")
            return
        
    print("not found ")
            
          
def update():
    roll = int(input("Enter roll to update marks: "))
    for s in students:
        if s["roll"] == roll:
            new_marks = int(input("Enter new marks: "))
            s["marks"] = new_marks
            print("✅ Marks updated successfully")
            return
        
        print("❌ Student not found")
        
        
        
    
def menu():
    while True:
        print("students data")
        print("1.add")
        print("2.display ")
        print("3.remove")
        print("4.search")
        print("5.update")
        print("6. exit")
        
        choice= input("enter choice ")
        
        if choice=="1":
            add_student()
        elif choice=="2":
            display()
            
        elif choice=="3":
            remove()
            
        elif choice =="4":
            search()
            
        elif choice== "5":
            update()
            
        elif choice == "6":
            break
        else:
            print("enter valid choice")
            
            
menu()




'''This program shows:
Data structures knowledge
CRUD operations
Menu handling
Clean coding style'''

'''This project demonstrates my understanding of data structures using list
and dictionary, full CRUD operations, menu-driven program design, 
and clean modular coding using functions. It simulates a real-world database system in Python.”'''

'''“I used list of dictionaries because it matches real-world database 
and JSON structures, keeps each student record self-contained, 
allows easy filtering and sorting, and provides uniform iteration.
Dictionary of dictionaries is suitable for fast direct lookup, 
but list of dictionaries is more flexible and closer to how data is stored and transferred in real applications.”'''

