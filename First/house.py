
name = input("What's your name? ")

# Match & Case - Harry Potter House
match name:
    case "Harry" |"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
