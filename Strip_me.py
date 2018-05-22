from cards import *
from adt_ import *
from time import sleep

# Made by Jordan Williams and Diandra Whittick


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


# a dictionary showing the value of pay cards
payCards = {'A':4,'K':3,'Q':2,'J':1} 

# test if it is a pay card or not
def isPayCard(card):
    return card[1] in payCards.keys()

# gets the rate of the pay card or return  if not
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
hand1 = new_Queue()

def prepPlayers():
    made_new_deck = new_Deck()
    shuffled = shuffle(5,made_new_deck)
    dealed_deck = deal(shuffled,26,2) 

    player0 = dealed_deck[0][0]
    player1 = dealed_deck[0][1]

    player0 = fillHand(hand,player0)
    player1 = fillHand(hand1,player1) 

    return player0,player1

# this function removes the top element of a players deck and adds it to the discard pile
def placeCard(A_players_Hand,stack): 
    temp_front = queue_front(A_players_Hand) 
    dequeue(A_players_Hand)
    push(stack,temp_front)

    return A_players_Hand,stack

# 
def playCard(curr_player,the_player_hand_of_cards,disc_pile): # the disc piles is the same stack used in the above program
   
    new = placeCard(the_player_hand_of_cards,disc_pile)
    a = the_player_hand_of_cards
    b = disc_pile
    print('')
    print ('Player %d ,' % curr_player)
    tup= new[1][1][0]
    print ('played the ',end='')
    
    print (tup[1]+getSuitIcon(tup[0]))
    print('\n \n')
      
    
    return a,b


def takePayment(playerHand,disc_pile):
    
    
    temp =new_Stack() 
    
    test = len(disc_pile[1])
    for x in range( test):
        t = stack_Top(disc_pile)
        pop(disc_pile)
        push(temp,t)

    
    t = stack_Top(temp)
    enqueue(playerHand,t)
    pop(temp)
 
    for x in range(len(stack_Contents(temp))):
        t = stack_Top(temp)
        pop(temp)
        push(disc_pile,t)

    return playerHand,disc_pile    

def strip_me():
    showGreeting()
    
    prep = prepPlayers() # creates a tuple of player 1 and 2 decks(shuffled)

    player1,player2 = prep # seperates the tuple to get player 1 and 2 

    s1 = new_Stack() #initialise of a stack for discard pile for player 1
    s2 = new_Stack() #initialise of a stack for discard pile for player 2
    
    
    # turn is used to manuplaulate who to play next
    # cont is varibale to store the choice of the player
    # rate1 represents the payment number for a card played by player1
    # rate 2 represents the payment number for a card played by player 2
    
    def game(turn,player1,player2,cont,rate1,rate2):  
        if empty_queue(player2): # shows the winner if player 1 wins
            print ('player 1 wins')
            return 'player 1 wins'

        elif empty_queue(player1): # shows the winner if player 2 wins
            print ('player 2 wins')
            return 'player 2 wins'


        elif cont == 'q': # exits the game
            print ('the game has ended')
            return 'the game has ended'

        elif cont.isalpha()== True: # if the user enters something he is not suppose to
            print ('incorrecnt input')
            return game(-1,player1,player2,'',rate1,rate2) 

        # if player 1 plays a pay card   
        elif rate1 > 0 and rate2 == 0 and turn == 1:
            sleep(1)    
            b = playCard(2,player2,s2)
            card_for_2 = b[1][1][0]
            cardRate2 = getCardRate(card_for_2)

            # if it happens that player 2 plays a paycard while he is paying it will break out and go back to the recursion
            if isPayCard(card_for_2): 
                return game(-1,player1,player2,'',0,cardRate2)

            here=len(s2[1]) 
            len_of_s1 = len(s1[1]) 

            rate1 -= 1  # this is to make sure the player 2 completes his payement

            # this is when the rate is fully paid it will give player 1 both player 2 discard pile and his own and print out who collected the discard pile
            if rate1 == 0:
                for x in range(here):
                    takePayment(player1,s2)
                for x in range(len_of_s1):
                    takePayment(player1,s1)   
               
                print('\nThe full payment was made. Player 1 claimed the discard pile')    
                return game(-1,player1,player2,'',rate1,rate2) 
                 
            return game(1,player1,player2,'',rate1,cardRate2) 

        # if player 2 plays a pay card
        elif rate1 == 0 and rate2 > 0 and turn == -1:
            sleep(1)    
            a = playCard(1,player1,s1)
            card_for_1 = a[1][1][0]
            cardRate1 = getCardRate(card_for_1)

            # if it happens that player 1 plays a paycard while he is paying it will break out and go back to the recursion
            if isPayCard(card_for_1):
                return game(1,player1,player2,'',cardRate1,0)

            there = len(s1[1])
            len_of_s2 = len(s2[1]) 
            rate2 -= 1
            # this is when the rate is fully paid it will give player 2 both player 1 discard pile and his own and print out who collected the discard pile
            if rate2 == 0:
                for x in range(there):
                    takePayment(player2,s1)
                for x in range(len_of_s2):
                    takePayment(player2,s2) 
                
                print('\n The full payment was made. Player 2 claimed the discard pile')    
                return game(1,player1,player2,'',rate1,rate2)     
            
            return game(-1,player1,player2,'',cardRate1,rate2)
        
        
        # this will run for player 2 if they were no pay cards played
        elif turn == 1 and rate1 ==0 and rate2 == 0: 
            b = playCard(2,player2,s2)
            card_for_2 = b[1][1][0]
            cardRate2 = getCardRate(card_for_2)
            
            return game(-1,player1,player2,'',rate2,cardRate2)

        # this will run for player 1 if they were no pay cards played
        elif turn == -1 and rate1 ==0 and rate2 == 0: 
            print('play(Enter); quit(q,then enter) ')
            cont = input ('Place your input: ')
            if cont == 'q':
                return game(-1,player1,player2,'q',rate1,rate2) 
            
            a = playCard(1,player1,s1)
            card_for_1 = a[1][1][0]
            cardRate1 = getCardRate(card_for_1)
            
            return game(1,player1,player2,'',cardRate1,rate2)
        else:
            print ('something went wrong')
            return ''
            

    # -1 represents the turn which when started will make player 1 play
    # player 1 is the hand of player 1
    # player 2 is the hand of player 2
    # '' which is a empty string is for cont
    # 0 represents the rate for player 1 and 2
    
    game(-1,player1,player2,'',0,0) #This calls the game function to run

strip_me()        
           
























       
    
    
