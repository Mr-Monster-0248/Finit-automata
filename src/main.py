from Automata import Automata
from utils_automata import *

loop = True
while loop:
    fa_choice = str(input("Choose a FA to test: "))
    filename = "../res/fa" + fa_choice + ".txt"

    fa = Automata(filename)

    print("Is asycronous: " + str(is_asynchronous(fa)))
    print("Is deterministic: " + str(is_deterministic(fa)))
    print("Is Complete: " + str(is_complete(fa)))
    print("Is standard: " + str(is_standard(fa)))

    print("testing a word")
    word = input("test word: ")

    print(read_word(fa, word))

    choice = input("Exit [y/n]? ")
    if choice == "n" or choice == "N":
        loop = True
    else:
        loop = False