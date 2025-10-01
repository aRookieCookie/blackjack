import time                 #To sleep the code so you don't spam the keys
import spel_onderdelen      #Script containing the classes
import subprocess           #for importing keyboard
import sys                  #for importing keyboard
import os                   #for clearing the screen
try:                                                                            #Try to
    import keyboard                                                             #import keyboard incase its already installed
except ImportError:                                                             #When there is an import error
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"]) #Run pip install keyboard in cmd
    import keyboard                                                             #Try the import again

def clear():                        #Function named clear
    os.system('cls')                #Clears the screen

def CalcPoints(hand):           #Function to calculate points of the set hand parameter
    all_ranks = []              #A list for sliced cards so it only contains letters and numbers
    rank_total_list = []        #A list containing only numbers (and translated letter's to numbers)
    rank_total = 0              #The sum of the list with only numbers
    ace_count = 0               #Amount of Aces in hand

    for i in range(len(hand)):              #for each card in hand
        all_ranks.append(hand[i][2:])       #Gets only the rank from a card (is a string) (for example: '♠️3' = '3', '♠️Q' = 'Q')

    for i in range(len(all_ranks)):                                                 #For all the ranks and letters only list
        if all_ranks[i].isdigit():                                                  #If its digit,
            rank_total_list.append(int(all_ranks[i]))                               #Add it to the rank_total_list as an int instead of string
        elif all_ranks[i] == 'J' or all_ranks[i] == 'Q' or all_ranks[i] == 'K':     #If its a picture card (except ace)
            rank_total_list.append(10)                                              #it adds a 10 to the list
        elif all_ranks[i] == 'A':                                                   #if its an ace it adds 1 to the ace count
            ace_count += 1                                                          #which will be later translated into the right amount
    rank_total = sum(rank_total_list)                                               #Gets an total of points in the current list (still excludes aces)

    if ace_count > 0 and rank_total < 11:                               #When there is an ace and the total is less than 11
        rank_total = sum(rank_total_list) + 11 + (ace_count - 1)        #Adds 11 points and the any other aces left will count for one
    elif ace_count > 0 and rank_total > 10:                             #If there is an ace and the score is 11 or higher
        rank_total = sum(rank_total_list) + ace_count                   #all aces become 1 point and gets added to the list and stored in rank_total

    return rank_total       #Sends back the total of points

def hands(player_hand, dealer_hand):                        #The game menu that shows everyone's hands
    clear()                                                 #Clears screen
    print('✨ BlackJack ✨')                               #Title
    print('=-==--=-==-=-=-=')                               #
    print('Dealer\'s Hand: ', end="")                       #Dealers hand:
    for i in dealer_hand.show_hand():                       #for each card in the dealers hand
        print(f'{i}, ', end="")                             #print the card with a ,
    print()                                                 #
    print('Total: ', CalcPoints(dealer_hand.show_hand()))   #Calculates the dealers total points and prints it under the cards
    print()                                                 #
    print('Player\'s Hand: ', end="")                       #Players hand:
    for i in player_hand.show_hand():                       #for each card in the players hand
        print(f'{i}, ', end="")                             #print the card with a ,
    print()                                                 #
    print('Total: ', CalcPoints(player_hand.show_hand()))   #Calculates the players total points and prints it under the cards
    print()                                                 #

def play_again():                                       #function to restart the game
    print('Do you want to play again? (y/n/b): ')       #Shows the option to play again
    while True:
        if keyboard.is_pressed('y'):                    #When y is pressed
            main()                                      #Restart the game
        elif keyboard.is_pressed('n'):                  #When n is pressed
            exit()                                      #Exit program
        elif keyboard.is_pressed('b'):                  #When b is pressed
            main_menu()                                 #Return to main menu

def rules():                                                                                                        #Function to explain the rules
    clear()                                                                                                         #Clears screen
    print('✨ BlackJack ✨')                                                                                       #Title
    print('=-==--=-==-=-=-=')                                                                                       #Seperator
    print()                                                                                                         #
    print('Goal:')                                                                                                  #Goal header
    print('Your goal is to get a score of 21 points.')                                                              #
    print('But be careful! One over and it\'s Game Over!')                                                          #
    print()                                                                                                         #
    print('Points:')                                                                                                #Points header
    print('Every card is worth its rank no matter the suit.')                                                       #
    print('Picture cards are 10 points and Ace 11. When you go over 21 an Ace turns into 1 point')                  #
    print()                                                                                                         #
    print('Actions:')                                                                                               #Actions header
    print('The player can Hit and Call. Hitting means you get a random card from the deck added to your hand')      #
    print('When you call, its the dealers turn, they will try to get a higher hand then yours')                     #
    print('When you have 21 points, you got yourself BlackJack! this means you won!')                               #
    print('You also win if the dealer busts. Which means they got over 21 points')                                  #
    print()                                                                                                         #
    print('Press Space to go back')                                                                                 #Space to go back
    time.sleep(0.2)                                                                                                 #Gives some time between the spacebar press in main menu and the rules so you dont get send instantly back
    while True:                                                                                                     #Keep waiting
        if keyboard.is_pressed('space'):                                                                            #is spacebar is pressed
            main_menu()                                                                                             #go to main menu


def main():                             #Main Game
    time.sleep(0.1)                     #Gives some time between clicking play and hit when spacebar is presed
    deck = spel_onderdelen.Deck()       #Creates all the cards by combining every suit with every rank in the class Deck
    spel_onderdelen.Deck.shuffle(deck)  #Shuffles the list deck

    options = ['Hit', 'Call']           #All options to that are selectable
    last_selected = -1                  #to check if selected is changed, so screen doesn't keep printing and clearing creating a flicker, starts at -1 so it initiates the first time
    selected = 0                        #the current selected option

    dealer_hand = spel_onderdelen.Dealer(deck)  #Add's 2 cards to the dealers hand
    player_hand = spel_onderdelen.Player(deck)  #Add's 2 cards to the players hand

    game_end = False        #shows current stage of the game, if its the dealers turn
    running = True          #shows current stage of the game, if dealers turn is needed/ended 

    while running:                                                                                              #Keeps playing so input can keep working
        if not last_selected == selected:                                                                       #If the last selected is different then current selected
            hands(player_hand, dealer_hand)                                                                     #It prints main interface of the game (Dealers/Players, points/hand)
            if not CalcPoints(player_hand.show_hand()) > 20 or not CalcPoints(dealer_hand.show_hand()) > 20:    #Makes the options available when the player still hasn't reached 21 or higher
                for option in range(len(options)):                                                              #for every possible option
                    if selected == option:                                                                      #if the selected is the current option
                        print(f'>{options[option]}<')                                                           #it prints it with ><
                    else:                                                                                       #otherwise
                        print(f'{options[option]}')                                                             #It prints just the option

                last_selected = selected                                                                        #Sets the last selected to selected so it doesn't need to print again
                                             #When i tried storing Calcpoints in variables, just creating the variable would break the dealer dealing cards even if the variable isn't used
        if not game_end:                                                        #If its still the players turn
            if keyboard.is_pressed('up'):                                       #When up arrow is pressed
                selected = (selected + 1) % len(options)                        #The selected will go 1 up, when its lower or higher than possible options it loops around because of the %
                last_selected = -1                                              #Sets last selected to -1 so it will print the again with updated selected
                time.sleep(0.1)                                                 #Sleeps the script so it doesn't spam input
            if keyboard.is_pressed('down'):                                     #When down arrow is pressed
                selected = (selected - 1) % len(options)                        #The selected will go 1 down and loop around
                last_selected = -1                                              #Sets last selected to -1 so it will print the again with updated selected
                time.sleep(0.1)                                                 #Sleeps the script so it doesn't spam input

            if keyboard.is_pressed('space') and selected == 0:                  #When spacebar is pressed and the selected is hit (first option)
                player_hand.hand.append(spel_onderdelen.Deck.deal(deck))        #it deals the first card in the deck and put it in the players hand
                last_selected = -1                                              #Sets last selected to -1 so it will print the again with updated hand
                time.sleep(0.1)                                                 #Sleeps the script so it doesn't spam input
            if keyboard.is_pressed('space') and selected == 1:                  #When spacebar is pressed and the selected is called (second option)
                game_end = True                                                 #It sets the game state into the dealers turn

        if CalcPoints(player_hand.show_hand()) > 21:                            #When player got +21 points
            hands(player_hand, dealer_hand)                                     #it prints the game for the last time with the exceeded cards
            print('🙈 You Busted! You Lost!')                                   #Tells the player the game is over
            running = False                                                     #Disables running so the game can be reset
        if CalcPoints(dealer_hand.show_hand()) == 21:                           #If the dealer gets 21 points
            hands(player_hand, dealer_hand)                                     #it prints the game for the last time with the exceeded cards
            print('🥶 Dealer Got a Blackjack! You Lost!')                       #Tells the player the game is over
            running = False                                                     #Disables running so the game can be reset
        if CalcPoints(player_hand.show_hand()) == 21:                           #When the player gets 21 points
            hands(player_hand, dealer_hand)                                     #it prints the game for the last time with all cards
            print('🐉 BLACKJACK! You Won!')                                     #Tells the player that the game is over
            running = False                                                     #Disables running so the game can be reset

        if game_end:                                                                                #When its the dealers turn
            while CalcPoints(player_hand.show_hand()) > CalcPoints(dealer_hand.show_hand()):        #When the player has a higher hand than the dealer
                hands(player_hand, dealer_hand)                                                     #print current cards
                time.sleep(1)                                                                       #Sleeps script for a second so the player can see what is happinging
                dealer_hand.hand.append(spel_onderdelen.Deck.deal(deck))                            #The dealer deals a card into its hand

            if CalcPoints(dealer_hand.show_hand()) > 21:                                            #If the dealer gets +21 points
                hands(player_hand, dealer_hand)                                                     #It shows the game with the exceeded cards
                print('🐼 Dealer Busted! You Won!')                                                 #Tells the player that the game is over
                break                                                                               #Breaks out of the running loop (same effect as running = false)
            elif CalcPoints(dealer_hand.show_hand()) == 21:                                         #If the dealer gets 21 points
                hands(player_hand, dealer_hand)                                                     #Shows the game with all cards
                print('🥶 Dealer Got a Blackjack! You Lost!')                                       #Tells player that the game is over
                break                                                                               #Breaks out of the running loop (same effect as running = false)
            elif CalcPoints(dealer_hand.show_hand()) > CalcPoints(player_hand.show_hand()):         #If the dealer has higher cards than the player
                hands(player_hand, dealer_hand)                                                     #Shows the game with all cards
                print('🦊 Dealer Wins! Higher Hand!')                                               #Tells player that the game is over
                break                                                                               #Breaks out of the running loop (same effect as running = false)
    play_again()                    #Ask's if the player wants to play again or return to main menu

def main_menu():                    #Function to draw the main menu
    time.sleep(0.1)                 #When going back from a game it sleeps so the spacebar press doesn't gets carried over
    last_selected = -1              #Same selection method as in the game
    selected = 0                    #current selected option

    options=['Play', 'Rules', 'Quit']   #All available options

    while True:
        if not last_selected == selected:           #If the last selected is not the same as the selected
            clear()                                 #Clears old stuff
            print('✨ BlackJack ✨')               #Title
            print('=-==--=-==-=-=-=')               #
            print()                                 #
            for option in range(len(options)):      #For every option
                if option == selected:              #If its the current selected option
                    print(f'>{options[option]}<')   #Print the option with ><
                else:                               #Otherwise
                    print(f' {options[option]}')    #Print the option
            print('\n\n')                           #
            print('Controls:')                      #Controls header
            print('⬆ Selection up')                 #Arrow up for selction change
            print('⬇ Selection down')               #Arrow down for selction change
            print('𓈙 Select')                      #Spacebar for select

            last_selected = selected                #Sets last selected to the selected so it only prints again when the selected is change to avoid flickering
            
        if keyboard.is_pressed('up'):                   #When up arrow is pressed
            selected = (selected - 1) % len(options)    #its scrolls to the options upwards
            time.sleep(0.1)                             #Sleeps the script so it doesn't spam the input
        if keyboard.is_pressed('down'):                 #When down arrow is pressed
            selected = (selected + 1) % len(options)    #its scrolls to the options upwards
            time.sleep(0.1)                             #Sleeps the script so it doesn't spam the input
        
        if keyboard.is_pressed('space') and selected == 0:  #When Play is selected (first option) and spacebar is pressed
            main()                                          #Start the game
        if keyboard.is_pressed('space') and selected == 1:  #When Rules is selected (second option) and spacebar is pressed
            rules()                                         #Open the rules
        if keyboard.is_pressed('space') and selected == 2:   #When Exit is selected (thirth option) and spacebar is pressed
            exit()                                          #Exits the program

main_menu()                                                 #First line thats gets executed when script starts 🥳, opens the main menu