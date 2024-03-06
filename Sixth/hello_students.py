students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)

for student in students:
    print(f"Hello, {student['name']} from {student['house']}")

"""for student in sorted(students):
    print(student)"""