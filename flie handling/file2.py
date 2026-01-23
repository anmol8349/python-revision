import csv
import json



with open ("students.csv","w",newline="") as f:
    writ=csv.writer(f)
    writ.writerow(["roll","name","marks"])
    writ.writerow([1,"anmol",95])
    writ.writerow([2,"Ram",66])
    


with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




data = {
    "name": "Anmol",
    "age": 22,
    "skills": ["Python", "AI", "Automation"]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
    


with open("data.json", "r") as f:
    data = json.load(f)
    print(data["name"])





try:
    with open("abc.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("Done")



