
# Main
def main():
    hello()
    name = input("What's your name? ")
    hello(name)

# Hello (to ) World
def hello(to="World"):
    print("Hello, ", to + "!")

    
main()
