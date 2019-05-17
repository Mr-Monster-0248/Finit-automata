class Automaton:
    """Class automaton"""

    def __init__(self):
        self.symboles = []
        self.states = {}
        self.initialStates = []
        self.finalStates = []
                
    def hasState(self, testState:int):
        return (testState in self.states)
    
    def hasSymbol(self, testSymbol:str):
        return (testSymbol in self.symboles)

    def hasInitialState(self, testInitialState:str):
        return (testInitialState in self.initialStates)
    
    def hasFinalStates(self, testFinalState:str):
        return (testFinalState in self.finalStates)

    def __str__(self):
        return ("Symboles: " + str(self.symboles) +
            "\nNumber of state: " + str(len(self.states)) +
            "\nInitial states: " + str(self.initialStates) + 
            "\nFinal states: " + str(self.finalStates))
    
    def toUML(self, output="output.txt"):
        # TODO
        pass
