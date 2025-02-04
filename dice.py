import time
import random

def start_game():
    number_of_players = int(input("How many players? "))

    players_names = []

    for i in range(number_of_players):
        player_name = input("Player " + str(i + 1) + ": ")
        players_names.append(player_name)

    print("\nAll players are here!")
    print("Welcome to the game: " + ", ".join(players_names) + "!\n")

    # countdown
    print("Loading...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("Game starting now!\n")

    def roll_dice_for_all_players():
        player_rolls = {}
        for player in players_names:
            player_rolls[player] = random.randint(1, 6)
        return player_rolls

    def reroll_in_rooms(player_rolls):
        rooms = {}
        for player, roll in player_rolls.items():
            if roll not in rooms:
                rooms[roll] = []
            rooms[roll].append(player)

        winners = []

        for roll, players in rooms.items():
            if len(players) == 1:
                winners.append((players[0], roll))
            else:
                print(f"\nTied players in room for roll {roll}: {', '.join(players)}. Re-rolling...\n")
                while len(players) > 1:
                    print("Re-rolling in this room...\n")
                    new_rolls = {player: random.randint(1, 6) for player in players}
                    print("New rolls for tied players:")
                    for player, roll in new_rolls.items():
                        print(f"{player} rolled a {roll}")

                    players = [player for player, roll in new_rolls.items() if roll == max(new_rolls.values())]
                    if len(players) == 1:
                        winners.append((players[0], new_rolls[players[0]]))
                    time.sleep(1)

        return winners

    player_rolls = roll_dice_for_all_players()

    print("Here are the rolls:\n")
    for player, roll in player_rolls.items():
        print(f"{player} rolled a {roll}")

    sorted_players = reroll_in_rooms(player_rolls)

    print("\nPlayer order based on dice rolls:")
    sorted_players = sorted(sorted_players, key=lambda x: x[1], reverse=True)
    for i, (player, roll) in enumerate(sorted_players, 1):
        print(f"{i}. {player} rolled a {roll}")

    first_player = sorted_players[0][0]
    print(f"\n{first_player} will start the game!\n")

    players_names = [player for player, roll in sorted_players]

    while len(players_names) > 0:
        for player in players_names[:]:
            roll_dice = input(f"{player}, do you want to roll the dice? (y/n): ").lower()

            if roll_dice == 'y':
                dice_roll = random.randint(1, 6)
                print(f"{player} rolled a {dice_roll}!\n")
            else:
                print(f"{player} decided not to roll the dice.\n")

                continue_game = input(f"{player}, do you want to continue the game? (y/n): ").lower()

                if continue_game == 'n':
                    players_names.remove(player)
                    print(f"{player} has been removed from the game.\n")

        if len(players_names) > 0:
            print("Game continues!\n")
        else:
            print("No players left. The game is over!")
            break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        start_game()
    else:
        print("Thanks for playing! Goodbye.")

start_game()
