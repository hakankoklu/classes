def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]

        # Write your code here

        while manSpouse[he] is None:
            she = hisPreferences[nextManChoice[he]]
            herPreferences = womenPreferences[she]
            currentHusband = womanSpouse[she]
            if currentHusband is None:
                manSpouse[he] = she
                womanSpouse[she] = he
                unmarriedMen.remove(he)
            else:
                if herPreferences.index(he) < herPreferences.index(currentHusband):
                    manSpouse[he] = she
                    womanSpouse[she] = he
                    manSpouse[currentHusband] = None
                    unmarriedMen.remove(he)
                    unmarriedMen.append(currentHusband)
                    nextManChoice[currentHusband] += 1
                else:
                    nextManChoice[he] += 1


        # Now "he" proposes to "she".
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice

    # Note that if you don't update the unmarriedMen list,
    # then this algorithm will run forever.
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse


# You might want to test your implementation on the following two tests:
assert (stableMatching(1, [[0]], [[0]]) == [0])
assert (stableMatching(2, [[0, 1], [1, 0]], [[0, 1], [1, 0]]) == [0, 1])
assert (stableMatching(3, [[0, 1, 2], [0, 2, 1], [0, 1, 2]], [[1, 2, 0], [2, 1, 0], [0, 2, 1]]) == [2, 0, 1])