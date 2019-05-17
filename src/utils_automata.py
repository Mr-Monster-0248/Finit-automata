from Automata import *

def is_synchronous(fa:Automata):
    for state in fa.states:
        for letter in fa.states[state]:
            if letter is "*":
                print(str(state) + " state has an * transition")
                return False
    return True

def is_deterministic(fa:Automata):
    if len(fa.initialStates) is not 1:
        return False
    elif is_asynchronous(fa):
        print("A asynchronous can't be deterministic")
        return False
    else:
        for letter in fa.symboles:
            for state in fa.states:
                if len(state[letter]) > 1:
                    return False
        return True