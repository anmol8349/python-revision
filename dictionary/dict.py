# A dictionary is a collection that stores data in  ------ key : value pairs.

# keys are unique 
# keys must be immutable
# values canbe any data type
# fast searching very efficient
student = {
    "name":"anmol",
    "age": 23
}

print(student)


d= dict(name="raMES", age=23)
print(d)

dd = {}
print(type(dd))   # <class 'dict'>


print(d["name"])

# safe access  using .get
print(student.get("age"))

d["city"]="gwl"
d["name"]="krishn"
print(d)


student.update({"age": 22, "marks": 90})


d.pop("age")
del d["name"]

# popitem    -- will del last inserted item 

# .clear remove all data




print(student.keys())

# print(student.values())

# print(student.items())

new_dict = student.copy()



# ---------looops  


for key in student:
    print("keys==",key)


for value in student.values():
    print(value)


for key, value in student.items():
    print(key, ":", value)


if "name" in student:
    print("Name exists")





# nested dict
students = {
    "s1": {"name": "Anmol", "age": 20},
    "s2": {"name": "Rahul", "age": 21}
}

print(students["s1"]["name"])   # Anmol


# dict with list
marks={
    "maths":[9,6,3,8,6,7],
    "science":[5,6,9,5,8,5]
    
}

# print(marks)
print(marks["maths"][2])





