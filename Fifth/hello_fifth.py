def main():
    name = input("What's your name? ")
    print(hello_f(name))

def hello_f(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()