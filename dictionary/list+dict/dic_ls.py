students =[
    {"roll":1, "name":"anmol","marks":99},
    {"roll":2, "name":"karl","marks":66},
    {"roll":3, "name":"suresh","marks":90}
]


# for s in students:
#     print(s)
    
    
# for s in students:
#     print(s["name"])
    
# for s in students:
#     print(f"Roll :{s["roll"]} || marks : {s["marks"]}") 
    
    
    # find roll 2
    
# r=2
# for s in students:
#     if s["roll"]==r:
#         print("found :" , s)
#         break
# else:
#     print("not found") 
    
    
for s in students:
    if s["roll"] == 3:
        s["marks"] = 88
        print("Updated:", s)
        
# for student in students:
#     if student["roll"] == 3:
#         print(student)


sorted_s = sorted(students,key = lambda x: x["marks"] , reverse=True)
# print(sorted_s)   # not a good way poora ek hi line me aa jayega


for s in sorted_s:
    print(s)