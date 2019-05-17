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
            for groupe in groupeList:
                for state in groupe:
                    tempGroupe.append([])
                    cpt = 0
                    for letter in fa.symboles:
                        tempGroupe[cpt].append(fa.states[state][letter])
                        cpt += 1
            print(tempGroupe)
            temp = groupeList

