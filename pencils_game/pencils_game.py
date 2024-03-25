"""project pencils game"""
import random

def main():
    """the main game cycle"""
    player_name = input("What's your name? >")
    while True:
        pencils_input = input("How many pencils would you like to use? > ")
        if not pencils_input.isdigit():
            print("The number of pencils should be numeric")
        elif int(pencils_input) <= 0:
            print("The number of pencils should be positive")
        else:
            pencils = int(pencils_input)
            break

    while True:
        first_player = input(f"Who will be the first? (Choose between {player_name} and Johnny!)> ")
        if first_player not in [player_name, 'Johnny']:
            print(f"Choose between {player_name} and 'Johnny'")
        else:
            break

    current_player = first_player

    while pencils > 0:
        print(f"{current_player}'s turn!")
        print("|" * pencils)
        if current_player == 'Johnny':
            if pencils % 4 == 0:
                taken_pencils = 3
            elif pencils % 4 == 3:
                taken_pencils = 2
            elif pencils % 4 == 1:
                taken_pencils = 1
            else:
                taken_pencils = random.randint(1, min(pencils, 3))
            print(taken_pencils)
        else:
            while True:
                taken_pencils = input("> ")
                if taken_pencils not in ['1', '2', '3']:
                    print("Possible values: '1', '2' or '3'")
                elif int(taken_pencils) > pencils:
                    print("Too many pencils were taken")
                else:
                    break

        pencils -= int(taken_pencils)

        if current_player == player_name:
            current_player = "Johnny"
        else:
            current_player = player_name

    if current_player == "Johnny":
        winner = "Johnny"
    else:
        winner = player_name
    print(f"{winner} won! ;)")


if __name__ == "__main__":
    main()

