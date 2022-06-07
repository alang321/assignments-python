from blackjack import genShuffledDeck, valueHand, nameCard

while True:
    print("\nBlackjack: beat the bank by getting as close to 21 as possible. Ace can count as 1 or 11, and jack, queen and king are 10 points")

    #new deck and reset values
    deck = genShuffledDeck()
    playerHand = []
    bankHand = []
    playerTotal = 0
    bankTotal = 0

    #player turn
    for i in range(0, len(deck)):
        playerHand.append(deck[i])
        playerTotal = valueHand(playerHand)

        print("\nYou get a ", nameCard(deck[i]), ". Your hand is worth ", playerTotal)

        if playerTotal >= 21 or input("\nDraw another card(Enter) or stop giving (’S + Enter’):") != "":
            break

    print("\nYour total is ", playerTotal)

    #bank turn
    if playerTotal <= 21:
        print("\nThe banks plays:\n")
        for j in range(i, len(deck)):
            bankHand.append(deck[j])
            bankTotal = valueHand(bankHand)

            print("Bank gets a ", nameCard(deck[j]), ". Bank is worth ", bankTotal)

            if bankTotal > playerTotal or bankTotal >= 21:
                break

    #win draw loose logic
    if playerTotal <= 21 and (playerTotal > bankTotal or bankTotal > 21):
        print("\nYou win!!")
    elif playerTotal == bankTotal:
        print("\nIts a draw :/")
    else:
        print("\nYou loose :(")

    #enter to play a new round
    if input("\nPress 'Enter' to play new round, 'E + Enter' to exit") != "":
        break