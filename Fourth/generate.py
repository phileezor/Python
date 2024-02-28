from random import choice
from random import randint
from random import shuffle
# import random

def main():
    # coin_flip()
    # rand_num()
    deck_c()
    print()

def coin_flip():
    coin = choice(["Heads", "Tails"])
    print(coin)

def rand_num():
    num = randint(1,10)
    print(num)

def deck_c():
    cards = ["Jack", "Queen", "King"]
    shuffle(cards)
    for card in cards:
        print(card)

main()