
def main():
    print_column(3)
    print()
    print_row(4)
    print()
    print_square(5)
    print()


def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

# Printing a super mario block-square
def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        print()

def better_print_square(size):

    # For each row in square
    for i in range(size):
            # Print brick
            print("#" * size, end="")
            
    print()


main()