from Automaton import *
from plantuml import *

test = Automaton("inputTest.txt")
print(test)
test.removeState(8)
print(test)

# Convert to an UML pic
# p = PlantUML()
# p.processes_file("output.txt")
