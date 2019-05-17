from Automata import Automata

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
    for state in fa.states:
        c = 0
        for char in fa.states[state]:
            c += 1
        if c != len(fa.symboles):
            return False
    return True

def read_word(fa:Automata, word:str, state=-1):
    for letter in word:
        if letter not in fa.symboles:
            return False
    if word == "" and state == -1:
        for init in fa.initialStates:
            if fa.has_finalStates(init):
                return True
        return False
    elif state == -1:
        for init in fa.initialStates:
            if not read_word(fa, word, init):
                continue
            else:
                return read_word(fa, word, init)
    elif word is "":
        if fa.has_finalStates(state):
            return True
        else:
            return False
    else:
        if word[0] not in fa.states[state]:
            return False
        else:
            nextState = fa.states[state][word[0]]
            print(nextState)
            if nextState is []:
                if fa.has_finalStates(state):
                    return True
                else:
                    return False
            else:
                for newstate in nextState:
                    if not read_word(fa, word[1:], newstate):
                        continue
                    else:
                        return read_word(fa, word[1:], newstate)
