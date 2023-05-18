

def findpokerhand(hand):

    ranks = []
    suits = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
        else:
            rank = card[0:2]
        print(rank)

    print(hand)
    return 0


if __name__ == "__main__":
    findpokerhand(["AH", "KH", "QH", "JH", "10H"]) # Royal Flush
    findpokerhand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush