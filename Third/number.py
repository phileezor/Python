
"""
# Can't handle strings... let's handle that
x = int(input("What's x? "))
print(f"x is {x}")
"""
# Error Handling - loop, try & except
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

"""
Remember to catch specific errors rather than all of them
"""

def main():
    x = get_int()
    print(f"x is {x}")
    y = better_get_int("What's y? ")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            # return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
            # pass - handles the error but no info is given to the user/reader
        else:
            return x

def better_get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
    

main()