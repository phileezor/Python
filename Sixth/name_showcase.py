
"""
Opening a new file and reading the lines into a variable then print them
to showcase and greet the person with the given name
"""

with open("name_collection.txt", "r") as file:
    for line in file:
        print(f"Hello, {line.rstrip()}. Glad you are back!")


"""
 |Slgiht Improvement of this above|

with open("name_collection.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"Hello, {line.rstrip()}. Glad to see you are back!")

"""