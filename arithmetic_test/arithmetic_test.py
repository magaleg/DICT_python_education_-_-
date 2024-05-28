
"""project arithmetic_test"""

import random


def generate_simple_task():
    """
    Generates a simple arithmetic task with two random numbers and a random operation.

    :return: tuple with a str for the question and int for the answer.
    """
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer


def generate_square_task():
    """
    Generates an integral square task for a random number from 11 to 29.

    :return: tuple with a str for the question and int for the answer.
    """
    num = random.randint(11, 29)
    question = f"{num}"
    answer = num ** 2
    return question, answer


def get_user_answer():
    """
    Asks user to input their answer.
    :return: inputted int
    """
    while True:
        user_input = input("Your answer: ")
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        else:
            print("Incorrect format. Please enter a number.")


def ask_question(question, correct_answer):
    """
    Shows the question, asks for an answer, then checks it.
    :param question: str, questions for the user.
    :param correct_answer: int, correct answer.
    :return: 1 if the asnwer is correct, 0 if it isn't.
    """
    print(question)
    user_answer = get_user_answer()
    if user_answer == correct_answer:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def arithmetic_test(level):
    """
    Test consists of 5 questions according to te level.

    :param level: int (1 or 2)
    :return: int (the number of correct answers)
    """
    score = 0
    for _ in range(5):
        if level == 1:
            question, answer = generate_simple_task()
        elif level == 2:
            question, answer = generate_square_task()
        score += ask_question(question, answer)
    print(f"Your mark is {score}/5.")
    return score


def save_result(name, score, level):
    """
    Saves the result to the "results.txt"

    :param name: str (user's name)
    :param score: int (the number of correct answers)
    :param level: int (level)

    """
    level_description = {
        1: "simple operations with numbers 2-9",
        2: "integral squares of 11-29"
    }
    with open("results.txt", "a") as file:
        file.write(f"{name}: {score}/5 in level {level} ({level_description[level]}).\n")
    print('The results are saved in "results.txt".')


def main():
    """
    The main function of the program.
    :return:
    """
    while True:
        try:
            level = int(input(
                "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    score = arithmetic_test(level)

    while True:
        save = input("Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()
        if save in ["yes", "y"]:
            name = input("What is your name?\n> ").strip()
            save_result(name, score, level)
            break
        elif save in ["no", "n"]:
            break
        else:
            print("Incorrect format.")


if __name__ == "__main__":
    main()


