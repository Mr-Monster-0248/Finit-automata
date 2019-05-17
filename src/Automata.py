import string

class Automata:
    """Class automaton"""

    def __init__(self, filename=""):
        if filename is "":
            self.symboles = []
            self.states = {}
            self.initialStates = []
            self.finalStates = []
        else:
            self.symboles = []
            self.states = {}
            self.initialStates = []
            self.finalStates = []
            try:
                content, transition, initial, final = self.read_automaton_from_file(filename)
            except Exception as e:
                print("Error loading the automata from file")
                raise e
            
            self.set_symboles(content[0])
            self.add_number_state(content[1])
            self.add_initials(initial)
            self.add_finals(final)
            self.add_transitions(transition)

    def set_symboles(self, size: int):
        for i in range(size):
            self.symboles.append(string.ascii_lowercase[i])

    def add_finals(self, final_list: list):
        for state in final_list:
            self.add_final(int(state))
    
    def add_final(self, finalState: int):
        if finalState not in self.finalStates:
            if finalState in self.states:
                self.finalStates.append(int(finalState))
            else:
                print(finalState + "state not in States of the FA")
        else:
            print(str(finalState) + "state already final")

    def remove_final(self, finalRemove):
        if finalRemove in self.finalStates:
            self.finalStates.remove(finalRemove)
        else:
            print(finalRemove + " not in final states")

    def add_initials(self, initial_list: list):
        for state in initial_list:
            self.initialStates.append(int(state))

    def add_number_state(self, size: int):
        self.states = dict.fromkeys(range(size))
        for state in self.states:
            self.states[state] = {}

    def add_transition(self, state: int, char, end_state: int):
        if char in self.states[state]:
            self.states[state][char].append(end_state)
        else:
            self.states[state][char] = [end_state]

    def add_transitions(self, transitions: list):
        for trans in transitions:
            self.add_transition(trans[0], trans[1], trans[2])
                
    def has_state(self, testState:int):
        return (testState in self.states)
    
    def has_symbol(self, testSymbol:str):
        return (testSymbol in self.symboles)

    def has_initialState(self, testInitialState:str):
        return (testInitialState in self.initialStates)
    
    def has_finalStates(self, testFinalState:str):
        return (testFinalState in self.finalStates)

    def read_automaton_from_file(self, filename: str):
        with open("../res/" + filename) as f:
            content = f.readlines()
            content = list(map(lambda s: s.strip(), content))

        # Show the file contents line by line.
        # We added the comma to print single newlines and not double newlines.
        # This is because the lines contain the newline character '\n'.
        if len(content) < 6:
            content = None
            raise Exception("Abort ! File is too small.")

        try:
            content[0] = int(content[0])
        except ValueError as e:
            content = None
            print("Can't read number of symbols in alphabet !")
            print("Error: " + str(e))

        try:
            content[1] = int(content[1])
        except ValueError as e:
            content = None
            raise Exception("Can't read number of states in alphabet ! Error: " + str(e))

        initial = content[2].split(" ")
        if int(initial[0]) == len(initial) - 1:
            del initial[0]
        else:
            initial = None
            raise Exception("Incorrect initial states!")

        final = content[3].split(" ")
        if int(final[0]) == len(final) - 1:
            del final[0]
        else:
            final = None
            raise Exception("Incorrect final states!")

        transitions = []
        for i in range(5, len(content)):
            transitions.append((int(content[i][0]), content[i][1], int(content[i][2])))

        return content, transitions, initial, final

    def __str__(self):
        return ("States:" + str(self.states) +
                "\nAlphabet: " + str(self.symboles) +
                "\nInitial states: " + str(self.initialStates) +
                "\nFinal states: " + str(self.finalStates))
    
    def toUML(self, output="output.txt"):
        # TODO
        pass
