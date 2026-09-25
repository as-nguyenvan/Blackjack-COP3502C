# Blackjack Program


# Import RNG
import p1_random as p1
rng = p1.P1Random()

#Variables
player_card = 0
player_hand = 0
dealer_hand = 0
player_wins = 0
dealer_wins = 0
ties = 0
number_of_games = 0
game_in_progess = True

# While 1 - Start Game Counter
while game_in_progess == True:
    number_of_games += 1
    player_hand = 0
    print(f"START GAME #{number_of_games}")
    player_card = rng.next_int(13) + 1
    if player_card == 1:
        player_card = "ACE"
        player_hand += 1
    elif 2 <= player_card <= 10:
        player_hand += player_card
    elif player_card == 11:
        player_card = "JACK"
        player_hand += 10
    elif player_card == 12:
        player_card = "QUEEN"
        player_hand += 10
    elif player_card == 13:
        player_card = "KING"
        player_hand += 10
    print()
    print(f"Your card is a {player_card}!")
    print(f"Your hand is {player_hand}")
    print()
    # While 2 - Game Options
    while True:
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
        print()
        user_input = int(input("Choose an option: "))

        if user_input == 1: # another card
            player_card = rng.next_int(13) + 1
            if player_card == 1:
                player_card = "ACE"
                player_hand += 1
            elif 2 <= player_card <= 10:
                player_hand += player_card
            elif player_card == 11:
                player_card = "JACK"
                player_hand += 10
            elif player_card == 12:
                player_card = "QUEEN"
                player_hand += 10
            elif player_card == 13:
                player_card = "KING"
                player_hand += 10
            print()
            print(f"Your card is a {player_card}!")
            print(f"Your hand is {player_hand}")
            print()

            if player_hand > 21:
                print("You exceeded 21! You lose.")
                print()
                dealer_wins += 1
                break
            elif player_hand == 21:
                print("BLACKJACK! You win!")
                print()
                player_wins += 1
                break

        elif user_input == 2: # hold hand
            dealer_hand = rng.next_int(11) + 16
            print()
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            if dealer_hand > 21:
                print("You win!")
                print()
                player_wins += 1
                break
            elif dealer_hand == 21:
                print("You lose!")
                print()
                dealer_wins += 1
                break
            elif dealer_hand == player_hand:
                print("Its a tie! No one wins!")
                print()
                ties += 1
                break
            elif dealer_hand < player_hand:
                print("You win!")
                print()
                player_wins += 1
                break
            elif dealer_hand > player_hand:
                print("You lose!")
                print()
                dealer_wins += 1
                break


        elif user_input == 3: # print stats
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {number_of_games}")
            percent_of_player_wins = (player_wins / number_of_games) * 100
            print(f"Percentage of Player wins: {percent_of_player_wins:.1f}%")
            print()
            continue

        elif user_input == 4: # exit
            game_in_progess = False
            break

        else:
            print("Invalid input!")
            print()
            print("Please enter an integer value between 1 and 4.")
            continue
