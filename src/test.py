from Automata import Automata as Automata
from utils_automata import *
# from plantuml import *

test = Automata("fa08.txt")
print(test)

print("Is asycronous: " + str(is_asynchronous(test)))
print("Is deterministic: " + str(is_deterministic(test)))

word = input("test word: ")

print(read_word(test, word))

# Convert to an UML pic
# p = PlantUML()
# p.processes_file("output.txt")
