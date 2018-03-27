import random

print('Welcome to the card game! What game would you like to play? Press 1 for blackjack, ')
menuAnswer = int(input('press 2 for war, or press 3 for go fish.'))
if menuAnswer == 1:
    print('Welcome to BlackJack!')
    print('--------------------Directions---------------------')
    print('You will be randomly assigned cards from the deck. The value of these cards will be ')
    print('calculated for you to keep track of. All face cards are equal to 10 and you will ')
    print('choose the value of aces at the end of the game. Good Luck!')
    J = 'J' and 10
    Q = 'Q' and 10
    K = 'K' and 10
    A = 'A' and 1 or 11
    totalDeck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, J, J, J, J, Q, Q, Q, Q, K, K, K, K, A, A, A, A]
    playerDeck = random.sample(totalDeck, 2)
    print(playerDeck)
    '''if J in playerDeck:
        J = int(10)
    if Q in playerDeck:
        Q = int(10)
    if K in playerDeck:
        K = int(10)'''
    playerValue = ('Your score is at ' + str(sum(playerDeck)))
    playerValueScore = int(sum(playerDeck))
    while 1==1:
        playerValue = ('Your score is at ' + str(sum(playerDeck)))
        playerValueScore = int(sum(playerDeck))
        print(playerValue)
        question1Answer = int(input('Do you want to draw another card? Press 1 for yes or 2 for no.'))
        turnCount = 0
        if question1Answer == 1:
            nextCard1 = random.sample(totalDeck, 1)
            playerDeck.extend(nextCard1)
            print(playerDeck)
            '''if J in playerDeck:
                J = int(10)
            if Q in playerDeck:
                Q = int(10)
            if K in playerDeck:
                K = int(10)'''
            playerValueScore = int(sum(playerDeck))
            playerValue = ('Your score is at ' + str(sum(playerDeck)))
            turnCount = turnCount + 1
            if playerValueScore > 21:
                print('Bust! ' + playerValue)
                break
            if playerValueScore <= 21:
                if turnCount >= 3:
                    print('You have 5 cards and a score under 21. You win!')
        if question1Answer == 2:
            print(playerValue)
            break
        
    
                   
