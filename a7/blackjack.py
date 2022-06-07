import random

#constants
decklength = 52
suitlength = 13

#generate shuffled deck and return
def genShuffledDeck():
    deck = list(range(0, decklength))
    random.shuffle(deck)
    return deck

#get name of card of given index and return
def nameCard(cardIndex):
    suits = ["diamonds", "hearts", "clubs", "spades"]
    cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

    return cards[cardIndex % suitlength] + " of " + suits[int(cardIndex / suitlength)]

#get the value of a card, assumes 1 for ace
def valueCard(cardIndex):
    return (cardIndex % suitlength + 1) if (cardIndex % suitlength) < 10 else 10

# Iterate over the cards in hand, calculates the total value and returns it
def valueHand(hand):
    values = list(range(0, len(hand)))

    for i in range(0, len(hand)):
        values[i] = valueCard(hand[i])
    total = sum(values)

    #if theres an ace in the hand and it doesnt go over 21 add 10
    if 1 in values:
        if total <= 11:
            total += 10

    return total