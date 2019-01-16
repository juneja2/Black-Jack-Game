
from card import Card
from players import Player
from random import randint
from os import system
from time import sleep

import shapes

def sleep_and_clear(seconds):
    sleep(seconds)
    system("cls")

def main_loop():
    total_bet_so_far = 0                                     # Create total bet variable

    prev_player_money = 100
    prev_dealer_money = 100
    while True:
        p, dealer = create_players(prev_player_money, prev_dealer_money)                             # create both players
        total_bet_so_far = change_total_bet_and_change_p_money(p, total_bet_so_far) # Ask for bet                       
        show_starting_cards(dealer, p)                           # Show starting cards  
        
        while True:
            if p.sum > 21:                                                      # Check if sum less than 21
                sleep_and_clear(0)
                dealer.print_player_cards(False)
                p.print_player_cards()
                print("Player busts. Dealer wins!!")
                dealer.money += total_bet_so_far
                break

            want_to_hit = input("Do you want to Hit or Stand. Enter Hit or Stand ").lower() == "hit"# Ask if user want to hit further
            if want_to_hit and p.money > 0 and dealer.money > 0:
                total_bet_so_far = change_total_bet_and_change_p_money(p, total_bet_so_far) # Ask for bet if use want to hit
                # Get betting amount and reduce player money, add it to the total bet, and set the betting_amount to 0 
                sleep_and_clear(1)
                p.append()          # Get a card for p and change the cards left in deck
                dealer.print_player_cards(False)
                p.print_player_cards()
            else:
                system("cls")
                dealer_cards_and_player_cards(dealer, p)
                display_winner(dealer, p, total_bet_so_far)
                sleep_and_clear(2)
                break

        if not wanna_play():                         # Ask player is he wants to play
            print("Total player money = " + str(p.money))
            print("Total dealer money = " + str(dealer.money))
            return
        else:
            prev_player_money = p.money
            prev_dealer_money = dealer.money
            total_bet_so_far = 0

def create_players(prev_player_money, prev_dealer_money):
    p = Player(prev_player_money)
    i = 0
    while i in range (2):
        p.append()
        i += 1
    dealer = Player(prev_dealer_money)       # Create both players
    dealer.append()

    return p, dealer

def change_total_bet_and_change_p_money(p, total_bet_so_far):
    betting_amount = get_betting_amount_for_player(p.money) # Get first bet
    p.money -= betting_amount                                           # Decrease money of player by that amount
    total_bet_so_far += betting_amount                                  # Keep track of total bet so you can give double when player wins
    return total_bet_so_far

def get_betting_amount_for_player(money_left):
    while True:
        bet = int(input("Place your bet. You have " + str(money_left) + " "))
        if bet <= money_left:
            return bet
        else:
            print("Invalid bet") 


def show_starting_cards(dealer, p):
    dealer.print_player_cards(player_turn=False)
    p.print_player_cards()


def dealer_cards_and_player_cards(dealer, p):
    while dealer.sum < 17:
        sleep_and_clear(2)
        dealer.append()
        dealer.print_player_cards()
        p.print_player_cards()
        

def display_winner(dealer, p, total_bet_so_far):
    if dealer.sum == p.sum:
        print("It is tie")
        p.money += total_bet_so_far

    elif dealer.sum < p.sum:
        print("Player wins")
        p.money += 2 * total_bet_so_far
        dealer.money -= total_bet_so_far

    elif dealer.sum > p.sum:
        if dealer.sum > 21:
            print("Dealer busts. Player wins!!")
            p.money += 2 * total_bet_so_far
            dealer.money -= total_bet_so_far
        else:
            print("Dealer wins")
            dealer.money += total_bet_so_far

def wanna_play():
    while True:
        yes_or_no = input("Do you want to play more. Enter Yes or No ").lower()
        if yes_or_no == "yes":
            return True
        elif yes_or_no == "no":
            return False
        else:
            print("Invalid choice. Please enter Yes or no ")

if __name__ == "__main__":
    main_loop()


