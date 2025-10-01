import time

import spel_onderdelen
import subprocess
import sys
import os
try:
    import keyboard
except ImportError:
    print("Installing 'keyboard' module")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
    import keyboard

def clear():
    os.system('cls')

def CalcPoints(hand):
    all_ranks = []
    rank_total_list = []
    rank_total = 0
    ace_count = 0

    for i in range(len(hand)):
        all_ranks.append(hand[i][2:])       #Gets only the rank from a card (is a string)
    # print('Hand Ranks: ', all_ranks)

    for i in range(len(all_ranks)):
        if all_ranks[i].isdigit():
            rank_total_list.append(int(all_ranks[i]))
        elif all_ranks[i] == 'J' or all_ranks[i] == 'Q' or all_ranks[i] == 'K':
            rank_total_list.append(10)
        elif all_ranks[i] == 'A':
            ace_count += 1
    # print('Hand Ranks: ', rank_total_list)
    rank_total = sum(rank_total_list)
    # print('Hand Rank Total: ', rank_total)

    if ace_count > 0 and rank_total < 11:
        rank_total = sum(rank_total_list) + 11 + (ace_count - 1)
    elif ace_count > 0 and rank_total > 10:
        rank_total = sum(rank_total_list) + ace_count

    return rank_total

def main():
    deck = spel_onderdelen.Deck()
    spel_onderdelen.Deck.shuffle(deck)

    options = ['Hit', 'Call']
    last_selected = -1
    selected = 0

    dealer_hand = spel_onderdelen.Dealer(deck)
    player_hand = spel_onderdelen.Player(deck)


    while True:
        if not last_selected == selected:
            clear()
            print('Dealer\'s Hand: ', dealer_hand.show_hand())
            print('Dealer\'s Hand Total: ', CalcPoints(dealer_hand.show_hand()))
            print('Player\'s Hand: ', player_hand.show_hand())
            print('Player\'s Hand Total: ', CalcPoints(player_hand.show_hand()))
            print()
            for option in range(len(options)):
                if selected == option:
                    print(f'>{options[option]}<')
                else:
                    print(f'{options[option]}')

            last_selected = selected

        if keyboard.is_pressed('up'):
            selected = (selected + 1) % len(options)
            time.sleep(0.1)
        if keyboard.is_pressed('down'):
            selected = (selected - 1) % len(options)
            time.sleep(0.1)

        if keyboard.is_pressed('space') and selected == 0:
            player_hand.hand.append(spel_onderdelen.hand.append(deck.deal()))


main()