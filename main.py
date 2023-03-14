from os import system
from art import logo
import random


def clear():
    _ = system('clear')


def play_game():
    user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user == 'y':
        clear()
        print(logo)
        return True
    else:
        return False


def draw_card(user_total, user_cards):
    draw = random.randint(0,11)
    user_cards.append(cards[draw])
    return card_check(user_total, draw)


def card_check(total, card):
    if card == 0:
        return ace(total)
    else:
        return cards[card]


def ace(total):
    if total + 11 > 21:
        return 1
    else:
        return 11


cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


play = play_game()

while play:
    total_player = 0
    total_dealer = 0
    computer_draw = True
    show_more = True
    not_done = True
    cards_player = []
    cards_dealer = []

    total_player += draw_card(total_player, cards_player)
    total_player += draw_card(total_player, cards_player)

    total_dealer += draw_card(total_dealer, cards_dealer)
    total_dealer += draw_card(total_dealer, cards_dealer)

    while not_done:
        print(f"    Your cards: {cards_player}, current score: {total_player}")
        print(f"    Computer's first card: {cards_dealer[0]}")

        not_done = input("Type 'y' to get another card, type 'n' to pass: ")
        if not_done == 'y':
            not_done = True
            total_player += draw_card(total_player, cards_player)
        else:
            not_done = False

        if total_player > 21:
            print(f"    Your cards: {cards_player}, final score: {total_player}")
            print(f"    Computer's final hand: {cards_dealer}, final score: {total_dealer}")
            print("You went over. You lose :( !")
            computer_draw = False
            show_more = False
            break

    while computer_draw and total_dealer < total_player and total_dealer < 17:
        total_dealer += draw_card(total_dealer, cards_dealer)

    if total_dealer > 21:
        print(f"    Your cards: {cards_player}, final score: {total_player}")
        print(f"    Computer's final hand: {cards_dealer}, final score: {total_dealer}")
        print("Computer went over. You win :) !")

    elif total_dealer > total_player:
        print(f"    Your cards: {cards_player}, final score: {total_player}")
        print(f"    Computer's final hand: {cards_dealer}, final score: {total_dealer}")
        print("Computer wins :( !")

    elif total_dealer == total_player:
        print(f"    Your cards: {cards_player}, final score: {total_player}")
        print(f"    Computer's final hand: {cards_dealer}, final score: {total_dealer}")
        print("You draw!")
    elif show_more:
        print(f"    Your cards: {cards_player}, final score: {total_player}")
        print(f"    Computer's final hand: {cards_dealer}, final score: {total_dealer}")
        print("You win :) !")

    play = play_game()
