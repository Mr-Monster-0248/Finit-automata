from Automata import Automata
from utils_automata import *

loop = True
while loop:
    fa_choice = str(input("Choose a FA to test: "))
    filename = "../fa/fa" + fa_choice + ".txt"

    fa = Automata(filename)

    print("testing a word")
    word = input("test word: ")

    print(read_word(fa, word))

    choice = input("Exit [y/n]? ")
    if choice == "n" or choice == "N":
        loop = True
    else:
        loop = False