def add_student():
    with open("students.txt", "a") as f:
        roll = input("Roll: ")
        name = input("Name: ")
        marks = input("Marks: ")
        f.write(f"{roll},{name},{marks}\n")

def show_students():
    with open("students.txt", "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")

while True:
    print("\n1. Add\n2. Show\n3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        show_students()
    elif ch == "3":
        break
