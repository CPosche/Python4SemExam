def findpokerhand(hand):

    ranks = []
    suits = []
    possibleRanks = []

    def case5():
        if suits.count(suits[0]) == 5:
            if 14 in sortedranks and 13 in sortedranks and 12 in sortedranks and 11 in sortedranks and 10 in sortedranks:
                possibleRanks.append(10)
            elif all(sortedranks[i] == sortedranks[i-1] + 1 for i in range(1, len(sortedranks))):
                possibleRanks.append(9)
            else:
                possibleRanks.append(6)
        #Straight
        elif all(sortedranks[i] == sortedranks[i-1] + 1 for i in range(1, len(sortedranks))):
            possibleRanks.append(5)
        
        else:
            possibleRanks.append(1)

    def case4():
        if len(handUniqueVals) == 4:
            possibleRanks.append(2)

    def case3():
        for val in handUniqueVals:
            if sortedranks.count(val) == 3:
                possibleRanks.append(4)
            if sortedranks.count(val) == 2:
                possibleRanks.append(3)

    def case2():
        for val in handUniqueVals:
            if sortedranks.count(val) == 4:
                possibleRanks.append(8)
            if sortedranks.count(val) == 3:
                possibleRanks.append(7)

    # Define a function to simulate switch case
    def switch_case(case):
        switch = {
            5: case5,
            4: case4,
            3: case3,
            2: case2
        }
    # Get the function corresponding to the case and execute it
        switch.get(case, lambda: print("Invalid case"))()

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        if rank == "A": rank=14
        elif rank == "K": rank=13
        elif rank == "Q": rank=12
        elif rank == "J": rank=11
        ranks.append(int(rank))
        suits.append(suit)

    sortedranks = sorted(ranks)
    handUniqueVals = list(set(sortedranks))
    switch_case(len(handUniqueVals))

    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush", 5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "One Pair", 1: "High Card"}
    output = (max(possibleRanks), pokerHandRanks[max(possibleRanks)])
    print(hand, output)
    return output