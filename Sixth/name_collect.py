# File I/O - saving the entered names into a file

name = input("What's your name? ")

"""
`with` can me used to open and close a file - 
a more pythonic way of coding since sometimes you can forget to close the file after using it
however `file = open("name_collection.txt", "a")`
"""

with open("name_collection.txt", "a") as file:
    file.write(f"{name}\n")