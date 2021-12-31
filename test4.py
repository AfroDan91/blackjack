def readCard(card):
    if "j" in card or "q" in card or "k" in card:
        return 10
    else:
        return int(card[1:])

print(readCard("a4"))