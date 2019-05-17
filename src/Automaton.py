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
                for i in range(len(self.transitions)):
                    self.transitions[i] = self.transitions[i][:3] #remove \n due to text reading
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

    def __str__(self):
        return ("Symboles: " + str(self.symbole) +
            "\nNumber of state: " + str(self.nbrState) +
            "\nInitial states: " + str(self.initialState) + 
            "\nFinal states: " + str(self.finalState) +
            "\nTransition" + str(self.transitions))
                
    def hasState(self, testState:int):
        return (testState in self.states)

    def hasTransition(self, testTransition:str):
        return (testTransition in self.transitions)
    
    def hasSymbol(self, testSymbol:str):
        return (testSymbol in self.symbole)

    def addTransition(self, startState:int, transitionSymbol:str, endState:int):
        if not self.hasSymbol(transitionSymbol):
            raise Exception("The symbol {} is not in the FA alphabet".format(transitionSymbol))
        elif not(self.hasState(startState) and self.hasState(endState)):
            raise Exception("{} or {} is not a state of the FA".format(startState, endState))
        else:
            newState = str(startState) + transitionSymbol + str(endState)
            self.transitions.append(newState)

    # Transition "code" stand for a string of 3 character representing the transition
    def addTransitionCode(self, newTransition:str):
        if len(newTransition) != 3:
            raise Exception("{} isn't a valide transition".format(newTransition))
        elif not(newTransition[0].isdigit() and self.hasState(int(newTransition[0])) and newTransition[2].isdigit() and self.hasState(int(newTransition[2]))):
            raise Exception("{} isn't a valide transition".format(newTransition))
        elif not self.hasSymbol(newTransition[1]):
            raise Exception("{} isn't a valide transition".format(newTransition))
        else:
            self.transitions.append(newTransition)
        
    def addTransitionList(self, newTransitionList:list):
        for code in newTransitionList:
            self.addTransitionCode(code)

    def removeTransition(self, transitionRemoved:str):
        if not self.hasTransition(transitionRemoved):
            raise Exception("{} transition not in FA".format(transitionRemoved))
        else:
            self.transitions.remove(transitionRemoved)

    def addState(self, newState:int):
        if self.hasState(newState):
            raise Exception("{} state already in FA".format(newState))
        else:
            self.states.append(newState)
            self.nbrState += 1
    
    def removeState(self, stateRemoved):
        if not self.hasState(stateRemoved):
            raise Exception("{} state not in FA".format(stateRemoved))
        else:
            self.states.remove(stateRemoved)
            self.nbrState -= 1

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
