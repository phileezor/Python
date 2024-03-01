names = []

with open("name_collection.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

# More concise, but more 'pythonic'
"""
with open("name_collection.txt", "r") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")
"""