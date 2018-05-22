# Written by Dr. Curtis Busby-Earle
# November 8, 2017

import random

# generate a random number between 0 and upperlimit
def genKey(upperlimit):
    return (random.randint(0,upperlimit))

# display a full deck of cards with suit icons
def displayDeck(deck):
    def empty_Deck(deck):
        return deck==[]
    def formatCard(card):
        return card[1]+getSuitIcon(card[0])    
    if empty_Deck(deck):
        raise Exception('Cannot display an empty deck of cards')
    else:
        formattedDeck=[formatCard(c) for c in deck]
        print (formattedDeck[:13],'\n',formattedDeck[13:26],'\n',formattedDeck[26:39],'\n', formattedDeck[39:])

# create a deck of 52 cards
def new_Deck():
    suits=["H","C","S","D"]
    facevalue=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    deck=[]
    for i in range(0,52):
        deck.append([])
    k=0    
    for i in range(0,4):
        for j in range(0,13):
            deck[k]=(suits[i],facevalue[j])
            k+=1
    return deck

#use the UNICODE value to display a suit
def getSuitIcon(suit):
    suitIcon={'H':u"\u2665",'C':u"\u2663",'S':u"\u2660",'D':u"\u2666"}
    return suitIcon[suit]

# shuffle repeatedly splits a deck in half, then interleaves the
# two half-decks together, nbrRounds times
def shuffle(nbrRounds,deck):

    #perform a left circular shift of the cards
    def circular_Shift(cards):
        el=cards[0]
        shiftedCards=cards[1:]
        shiftedCards.append(el)
        return shiftedCards

    #perform nbrPositions repeated circular shifts of the cards
    def shift_Cards(nbrPositions,cards):
        if cards!=[]:
            for ctr in range(nbrPositions):
                cards=circular_Shift(cards)
        return cards

    # split takes a deck as input and splits it into two halves
    def split(deck):
        nbrCards = len(deck)
        return (deck[0:int(nbrCards/2)],deck[int(nbrCards/2):])

    # interleave takes a pair of half-decks as input and returns a new deck
    # The new deck contains all the items of the input half-decks,
    # but with their cards shifted a random number of times
    # then repositioned in alternating order
    def interleave(half_decks):
        hd1,hd2 = half_decks
        if hd1 == []:
            return hd2
        elif hd2 == []:
            return hd1
        else:
            hd1,hd2=shift_Cards(genKey(int(len(hd1))),hd1),shift_Cards(genKey(int(len(hd2))),hd2)
            return [hd1[0]]+[hd2[0]] + interleave((hd1[1:],hd2[1:]))
    
    if  nbrRounds==0:
        return deck
    else:
        return shuffle(nbrRounds - 1, interleave(split(deck)))

# Using deck of cards 'deck', deal 'nbrCards' cards to each of the 'nbrPlayers' players
# Return the tuple [[a list of lists, where each list represents the hand of each player],[list of cards that have not been dealt]]

def deal(deck,nbrCards,nbrPlayers):
    if nbrCards*nbrPlayers <= len(deck):
        dealtCards=[]
        for i in range(0,nbrPlayers):
            dealtCards.append([])
        for i in range(0,nbrCards):
            for j in range(0,nbrPlayers):
                dealtCards[j].append(deck.pop())
        return dealtCards,deck
    else:
        raise Exception("Not enough cards in the deck")





























from itertools import cycle



def new_Queue():
    return 'queue',[]
def is_Queue(q):
    return type(q) == type(()) and q[0] == 'queue'
def queue_Contents(q):
    return q[1]
def empty_queue(q):
    return queue_Contents(q) == []
def queue_front(q):
    return queue_Contents(q)[0]
def enqueue(q,el):
    queue_Contents(q).append(el)
def dequeue(q):
    queue_Contents(q).pop(0) #changed to pop


def new_Stack():
    return 'stack',[]
def is_Stack(s):
    return type(s)== type(()) and s[0] == 'stack'
def stack_Contents(s):
    return s[1]
def empty_Stack(s):
    return stack_Contents(s) == []
def stack_Top(s):
    return stack_Contents(s)[0]
def push(s,el):
    stack_Contents(s).insert(0,el)
def pop(s):
    stack_Contents(s).pop(0)

def showGreeting():
        print ('********************************************************')
        print ('* Created by Jordan Williams and Diandra Whittick      *')                          
        print ('*                                                      *')
        print ('* WELCOME to Strip Me                                  *')
        print ('*                                                      *')
        print ('* Rules of the game: Check the docs                    *')
        print ('*                                                      *')
        print ('* Game Play:                                           *')
        print ('* - player 0: the computer                             *')
        print ('* - player 1: you                                      *')
        print ('* - enter: play the top card and place on discard pile *')
        print ('* - q: quit i.e. stop playing the game *                ')
        print ('*                                                      *')
        print ('* Enjoy!                                               *')
        print ('********************************************************')

payCards = {'A':4,'K':3,'Q':2,'J':1}

def isPayCard(card):
    return card[1] in payCards.keys()
def getCardRate(card): 
    if isPayCard(card):
        return payCards[card[1]]
    else:
        return 0

def fillHand(q,lst):
    for x in lst:
        enqueue(q,x)
    return q

hand = new_Queue()

def prepPlayers():
    made_new_deck = new_Deck()
    shuffled = shuffle(5,made_new_deck)
    dealed_deck = deal(shuffled,26,2)

    player0 = dealed_deck[0][0]
    player1 = dealed_deck[0][1]

    player0 = fillHand(hand,player0)
    player1 = fillHand(hand,player1) # just changed it to 'hand' from q

    return player0,player1

# this function removes the top element of a players deck and adds it to the discard pile
def placeCard(A_players_Hand,stack): # test data placeCard(what[1],new_Stack())
    temp_front = queue_front(A_players_Hand) 
    dequeue(A_players_Hand)
    push(stack,temp_front)

    return A_players_Hand,stack

# 
def playCard(curr_player,the_player_hand_of_cards,disc_pile): # the disc piles is the same stack used in the above program
    a = the_player_hand_of_cards
    b = disc_pile
    new = placeCard(the_player_hand_of_cards,disc_pile)
    
    print ('Player %d ,' % curr_player)
    tup= new[1][1]
    print ('played the ',end='')
    print (displayDeck(tup))
    '''if len(displayDeck(tup)[0]) == 1:
        print (displayDeck(tup)[0][0])
    else:
        print (displayDeck(tup))  '''    
    
    return a,b

def make_pile(playerhand):
    return playerhand[1][1][0]
def make_hand(playerhand):
    return playerhand[0]

def takePayment(playerHand,disc_pile):
    #lst = [stack_Top(disc_pile)]
    #queue_Contents(playerHand).insert(len(queue_Contents(playerHand)),stack_Top(disc_pile))# takePayment(a[0],stack_Contents(a[1]))
    #enqueue(playerHand,disc_pile)
    '''*for x in queue_Contents(playerHand):
        lst.append(x)

    lst = ('queue',lst,[('stack',disc_pile[1][0]]) )
    return lst
    '''
    t=stack_Top(disc_pile)

    print (t)

    pop(disc_pile)
    enqueue(playerHand,t)
    return playerHand,disc_pile

def strip_me():
    showGreeting()
    
    prep = prepPlayers() # creates a tuple of player 1 and 2 decks(shuffled)

    player1,player2 = prep # seperates the tuple to get player 1 and 2 

    q1 = new_Stack() #initialise of a stack q1 and q2
    q2 = new_Stack()
    
    #player1_pile = placeCard(player1,q1) # this is the player with their pile

   # player2_pile = placeCard(player2,q2) 
    
    play_or_quit = input('play(Enter); quit(q,then enter) ')


    # prompts the user to Play or Quit
    if play_or_quit.lower() == '':      
        test = True
    elif play_or_quit.lower() == 'q':
        test = False
    else:
        print('you entered a wrong ')
        test = False

    while test == True:
        str1 = input("")
        if str1 == 'q':
            break
        elif empty_queue(player1):
            print('player 1 wins')
            break
        elif empty_queue(player2):
            print('player 2 wins')
            break
        else:
            #playCard(1,player1,q1)
            for turn in cycle((playCard(1,player1,q1),playCard(2,player2,q2))):
                str1 = input("type q if you wanna quit or hit Enter to continue")
                if str1 == 'q':
                    break
                elif empty_queue(player1):
                    print('player 1 wins')
                    break
                elif empty_queue(player2):
                    print('player 2 wins')
                    break
                else:
                    print('')
                    turn
                
        
                
             
                    
                
            
        
    
