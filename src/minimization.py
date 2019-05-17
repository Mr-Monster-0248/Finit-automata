from Automata import Automata
from utils_automata import is_complete

def minimization(fa:Automata):
    if not is_complete(fa):
        print("c pa possible")
    else:
        groupeList = []
        groupeList.append([])
        for final in fa.finalStates:
            groupeList[0].append(final)

        groupeList.append([])
        for state in fa.states:
            if not fa.has_finalStates(state):
                groupeList[1].append(state)
        
        print(groupeList)
        temp = []
        while (temp != groupeList):
            tempGroupe = []
            print(tempGroupe)
            temp = groupeList

