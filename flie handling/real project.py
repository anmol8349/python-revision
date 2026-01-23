import json
from datetime import datetime

students={}   #empty dict  , roll as key

   
# save to file -------------


def save_data(data):
    with open("students.json",'w') as f:
        json.dump(data,f,indent=4)
        
def load_data():
    try:
        with open ("students.json",'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return{}
    
    
    
def add_student():
    
    data = load_data()
    
    
    roll=input("enter roll: ")
    if roll in data:
        print("Roll already exists!")
        return
    
    name=input("enter name: ")
    
    
    while True:
        marks_input = input("enter marks: ").strip()
        if marks_input.isdigit():
            marks = int(marks_input)
            break
        else:
            print("❌ Marks must be a valid number")
    
    
    grade = calculate_grade(marks)
    data[roll] ={
        "name" : name,
        "marks": marks,
        "grade":grade,
        "created_at": str(datetime.now())
        
    }
    
    
    save_data(data)
    print("student saved")
    
   
   
def search_student():
    data = load_data()
    
    roll=input("enter roll: ")
    
    if roll in data:
        print(data[roll])
    else:
        print("Not found ")
        
        
def update_student():
    data =load_data()
    roll =input("enter roll: ")
    
    if roll not in data:
        print("Not found")
        return
    
    name = input("New name (blank to skip): ")
    marks = input("New marks (blank to skip): ").strip()
    
    updated = False
    
    
    if name:
        data[roll]["name"]=name
        updated=True
        
    if marks:
        try:
            marks = float(marks)
            if 0 <= marks <= 100:
                marks = int(marks)
                data[roll]["marks"] = marks
                data[roll]["grade"] = calculate_grade(marks)
                updated = True
            else:
                print("❌ Marks must be between 0 and 100")
                return
        except ValueError:
            print("❌ Invalid marks input")
            return
        
    if updated:
        data[roll]["updated_at"]=str(datetime.now())
        save_data(data)
        print("updated")
        
    else:
        print("no changes made")
        

        

    


def delete_student():
    data = load_data()
    roll = input("Enter roll: ")

    if roll in data:
        del data[roll]
        save_data(data)
        print("Deleted")
    else:
        print("Not found")


    
def calculate_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 75: return "A"
    elif marks >= 60: return "B"
    elif marks >= 50: return "C"
    else: return "F"
    


 

def sort_students():
    data=load_data()
    
    key = input("sort by (name/marks/grade): ")
    reverse = input("descending? y/n: ") == "y"

    sorted_data =sorted(
        data.items(),
        key = lambda x: x[1][key],
        reverse=reverse
    )
    
    for roll, info in sorted_data:
        print(roll, info)
    
    
    
    

def display_students():
    data = load_data()
    if not data:
        print("No records found")
        return


    print("\nRoll | Name | Marks | Grade")
    print("-" * 40)
    for roll, info in data.items():
        print(f"{roll} | {info['name']} | {info['marks']} | {info['grade']}")
    
    

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Exit")
        
        
        
        choice =input("enter choice : ")
        
        match choice:
            case '1': add_student()
            case '2': display_students()
            case '3': search_student()
            case '4': update_student()
            case '5': delete_student()
            case '6': sort_students()
            case '7':
                    print("tata exiting")
                    break
            case _:
                print("invalid choice ")
       
            
menu()