from Automata import Automata as Automata
from minimization import *
# from plantuml import *

test = Automata("fa13.txt")
print(test)

test.toFile()

# Convert to an UML pic
# p = PlantUML()
# p.processes_file("output.txt")
