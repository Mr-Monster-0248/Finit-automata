from Automata import *

def is_asynchronous(fa:Automata):
    for state in fa.states:
        for letter in fa.states[state]:
            if letter is "*":
                print(str(state) + " state has an * transition")
                return True
    return False

def is_deterministic(fa:Automata):
    if len(fa.initialStates) is not 1:
        return False
    elif is_asynchronous(fa):
        print("A asynchronous can't be deterministic")
        return False
    else:
        for state in fa.states:
            for char in fa.states[state]:
                if len(fa.states[state][char]) > 1:
                    return False
        return True

def is_complete(fa:Automata):
    pass
