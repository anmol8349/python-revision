students={}

n = int(input("enter number of students"))

for i in range (n):
    roll= input("enter roll  ")
    marks = int(input("enter marks "))
    
    students[roll] = marks
    
    
for roll,marks in students.items():
    print("roll ",roll ,'marks =',marks)
    
    
for roll, marks in sorted(students.items(), key=lambda x: x[1], reverse=True):
    print("Roll No:", roll, "Marks:", marks)

