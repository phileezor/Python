"""
# Loops - While
i = 0
while i < 3:
    print("while - meow")
    i += 1
print("\n", end="")

# Loops - For
for a in range(3):
    print("for - meow")
print("\n", end="")

# Iterated Print
print("iterated - meow\n" * 3, end="")

# Readers input - While & For
while True:
    n = int(input("\nWhat's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Readers - meow")

"""

def main():
    num = get_number()
    meow(num)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Reader says: meow")

main()