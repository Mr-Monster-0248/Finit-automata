class Automaton:
    """Class automaton"""

    def __init__(self, filepath="", nbrSymbole=0, nbrState=0, nbrInitialState=1, initialState=[], nbrFinalState=0, finalState=[], nbrTransitions=0, transitions=[]):
        if filepath != "":
            with open(filepath, "r") as f:
                self.nbrSymbole = int(f.readline())
                self.symbole = []
                for i in range(self.nbrSymbole):
                    self.symbole.append(chr(i + 97))
                self.nbrState = int(f.readline())
                self.states = []
                for i in range(self.nbrState):
                    self.states.append(i)
                self.initialState = f.readline().split(" ")
                self.nbrInitialState = len(self.initialState)
                for i in range(self.nbrInitialState):
                    self.initialState[i] = int(self.initialState[i])
                self.finalState = f.readline().split(" ")
                self.nbrFinalState = len(self.finalState)
                for i in range(self.nbrFinalState):
                    self.finalState[i] = int(self.finalState[i])
                self.transitions = f.readlines()
                self.nbrTransitions = len(self.transitions)
        else:
            self.nbrSymbole = nbrSymbole
            self.symbole = []
            for i in range(self.nbrSymbole):
                self.symbole.append(chr(i + 97))
            self.nbrState = nbrState
            self.states = []
            for i in range(self.nbrState):
                self.states.append(i)
            self.nbrInitialState = nbrInitialState
            self.initialState = initialState
            self.nbrFinalState = nbrFinalState
            self.finalState = finalState
            self.nbrTransitions = nbrTransitions
            self.transitions = transitions

    def describe(self):
        print("Symboles: {", end=" ")
        for symb in self.symbole:
            print(symb, end=",")
        print("}")
        print("Number of state: ", self.nbrState)
        print("States: {", end=" ")
        for state in self.states:
            print(state, end=",")
        print("}")
        print("Number of initial states: ", self.nbrInitialState)
        print("Number of final states: ", self.nbrFinalState)
        print("Number of transitions: ", self.nbrTransitions)
        print("Transition: {", end=" ")
        for trans in self.transitions:
            print(trans)
        print("}")

    def toUML(self, output="output.txt"):
        with open(output, "w") as outputfile:
            outputfile.write("@startuml\n")
            outputfile.write("hide empty description\n")
            for init in self.initialState:
                outputfile.write("[*] --> ")
                outputfile.write(str(init))
                outputfile.write("\n")
            for final in self.finalState:
                outputfile.write(str(final))
                outputfile.write(" --> [*]")
                outputfile.write("\n")
            for transi in self.transitions:
                outputfile.write(transi[0])
                outputfile.write(" --> ")
                outputfile.write(transi[2])
                outputfile.write(" : ")
                outputfile.write(transi[1])
                outputfile.write("\n")
            outputfile.write("@enduml")
