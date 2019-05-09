from Automaton import *
from plantuml import *

test = Automaton("inputTest.txt")
test.describe()
test.toUML()
p = PlantUML()
p.processes_file("output.txt")
