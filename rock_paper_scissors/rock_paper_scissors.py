""" project rock paper scissors"""

import random


def read_ratings(file_name):
    """
    Reads the ratings from a file and returns them as a dictionary.

    :param file_name: str, file name
    :return: dict (usernames for keys, ratings for values)
    """
    ratings = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                name, score = line.split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings


def write_ratings(file_name, ratings):
    """
    Writes the ratings to a file.

    :param file_name: str, file name
    :param ratings: dict, (usernames for keys, ratings for values)
    """
    with open(file_name, "w") as file:
        for name, score in ratings.items():
            file.write(f"{name} {score}\n")


def display_ratings(ratings):
    """
    Displays the ratings of all players.

    :param ratings: dict, (usernames for keys, ratings for values)
    """
    print("Current ratings:")
    for name, score in ratings.items():
        print(f"{name}: {score}")


def determine_winner(user_choice, computer_choice, options):
    """
    Determines the winner of a game round

    :param user_choice: str, the user's choice
    :param computer_choice: str, the computer's choice
    :param options: list,
    :return: str, the result.
    """
    if user_choice == computer_choice:
        return "draw"

    index = options.index(user_choice)
    new_order = options[index + 1:] + options[:index]
    half = len(new_order) // 2

    if computer_choice in new_order[:half]:
        return "lose"
    else:
        return "win"


def play_game(user_choice, user_score, options):
    """
    Plays a round of the game, updates the user's score based on the result, and prints the result.

    :param user_choice: str, the user's choice
    :param user_score: int, the user's current score.
    :param options: list of all possible game options.
    :return: tuple, the updated user score and the result of the game round.
    """
    computer_choice = random.choice(options)

    if user_choice not in options:
        print("Invalid input")
        return user_score, None

    result = determine_winner(user_choice, computer_choice, options)
    if result == "draw":
        print(f"There is a draw ({computer_choice})")
        user_score += 50
    elif result == "win":
        print(f"Well done. The computer chose {computer_choice} and failed")
        user_score += 100
    else:
        print(f"Sorry, but the computer chose {computer_choice}")

    return user_score, result


def main():
    """
    Main function of the game.
    """
    ratings = read_ratings("rating.txt")

    user_name = input("Enter your name: ").strip()
    print(f"Hello, {user_name}")

    user_score = ratings.get(user_name, 0)

    display_ratings(ratings)

    options_input = input("Enter options (comma separated) or leave empty for default: ").strip().lower()
    if options_input == "":
        options = ["rock", "paper", "scissors"]
    else:
        options = [option.strip() for option in options_input.split(',')]

    while len(options) % 2 != 1 or len(options) <= 3:
        print("Please enter an odd number of options more than 3.")
        options_input = input("Enter options (comma separated) or leave empty for default: ").strip().lower()
        if options_input == "":
            options = ["rock", "paper", "scissors"]
        else:
            options = [option.strip() for option in options_input.split(',')]

    print("Okay, let's start")

    while True:
        user_input = input("Enter an option, !rating or !exit: ").strip().lower()
        if user_input == "!exit":
            print("Bye!")
            ratings[user_name] = user_score
            write_ratings("rating.txt", ratings)
            break
        elif user_input == "!rating":
            print(f"Your rating: {user_score}")
        else:
            user_score, result = play_game(user_input, user_score, options)
            if result is not None:
                ratings[user_name] = user_score
                write_ratings("rating.txt", ratings)


if __name__ == "__main__":
    main()
