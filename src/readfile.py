def read_automaton_from_file(filename: str):
    with open("../fa/" + filename) as f:
        content = f.readlines()
        content = list(map(lambda s: s.strip(), content))

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contain the newline character '\n'.
    if len(content) <= 6:
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