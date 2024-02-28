
# List - list
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Dictionary I - dict
students_dict = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

# Dictionary II - dict
students_dictx = [
    {"name": "Hermione", "house":"Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus": None}
]

# Dictionary I - Loop
print()
for student in students_dict:
   print(student, students_dict[student], sep=": ")
print()

# Dictionary II - Loop
for student in students_dictx:
    print(student["name"], student["house"], student["patronus"], sep =" | ")
print()

"""
# Loop over the list - I
for student in students:
    print(student)

# Loop over the list - II
for i in range(len(students)):
    print(i + 1, ". " + students[i], sep="")
"""