import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_drawing = False
lets_play = True
user_card = []
computer_card = []

def draw_card():
    user_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))

def play_or_not():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":

        global keep_drawing
        global lets_play
        keep_drawing = True
        lets_play = True
    else:
        keep_drawing = False
        lets_play = False

def play_again():
    play = input("Type 'y' to get another card, type 'n' to pass: ")
    if play == "y":
        global keep_drawing
        keep_drawing = True

    if play == "n":
        keep_drawing = False

        if user_total() == computer_total():
            print(f"Your final hand {user_card}, final score = {user_total()}")
            print(f"Computer's final hand {computer_card}, final score = {computer_total()}")
            print("It's a draw!!")
        if (21 - user_total()) < (21 - computer_total()):
            print(f"Your final hand {user_card}, final score = {user_total()}")
            print(f"Computer's final hand {computer_card}, final score = {computer_total()}")
            print("You won!! 🏆")
        elif (21 - user_total()) > (21 - computer_total()):
            print(f"Your final hand {user_card}, final score = {user_total()}")
            print(f"Computer's final hand {computer_card}, final score = {computer_total()}")
            print("You lose!!")

def check_if_over_21():
    global keep_drawing
    if user_total() > 21:
        keep_drawing = False

    elif computer_total() > 21:
        keep_drawing = False

    else:
        keep_drawing = True

def user_total():
    user_sum = 0
    ace_counter = 0
    for card in user_card:
        if card == 11:  # Ace
            ace_counter += 1
            user_sum += 11
        else:
            user_sum += card

    while user_sum > 21 and ace_counter > 0:
        user_sum -= 10
        ace_counter -= 1
        user_card[user_card.index(11)] = 1

    return user_sum

def computer_total():
    comp_sum = 0
    ace_counter = 0
    for card in computer_card:
        if card == 11:  # Ace
            ace_counter += 1
            comp_sum += 11
        else:
            comp_sum += card

    while comp_sum > 21 and ace_counter > 0:
        comp_sum -= 10
        ace_counter -= 1
        computer_card[computer_card.index(11)] = 1



    return comp_sum

def result():
    if user_total() > 21:
        print(f"Your final hand {user_card}, final score = {user_total()}")
        print(f"Computer's final hand {computer_card}, final score = {computer_total()}")
        print("You went over. You lose 😭")
    elif computer_total() > 21:
        print(f"Your final hand {user_card}, final score = {user_total()}")
        print(f"Computer's final hand {computer_card}, final score = {computer_total()}")
        print("Your opponent went over. You win 🏆")


def the_game():
    while keep_drawing:
        draw_card()
        check_if_over_21()

        while computer_total() < 17:
            computer_card.append(random.choice(cards))

        if not keep_drawing:
            continue
        print(f"Your cards: {user_card}, current score = {user_total()}")
        print(f"Computer's first card: {computer_card[0]}")

        if keep_drawing:
            play_again()
    result()

while lets_play:
    play_or_not()
    if lets_play:
        print("\n" * 50)
        print(art.logo)
        draw_card()
        the_game()
        user_card.clear()
        computer_card.clear()








