from Automata import Automata as Automata
from minimization import *
# from plantuml import *

test = Automata("fa08.txt")
print(test)

minimization(test)

# Convert to an UML pic
# p = PlantUML()
# p.processes_file("output.txt")
